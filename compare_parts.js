const fs = require('fs');
const { parse } = require('csv-parse/sync'); // Using sync version for simplicity

// --- Configuration ---
// Adjust these paths if your files are located elsewhere
const shoppingListPath =
  '/Users/wangzengdi/Projects/Adi/browser-use-taobao/rebrickable/MOC-13349_compact_tracked_loader (2).csv';
const taobaoCartPath =
  '/Users/wangzengdi/Projects/Adi/browser-use-taobao/rebrickable/淘宝-2025-04-14-12-55-04.csv';

// Column indices (0-based) for Part ID, Quantity, and Color
const shoppingListIdCol = 0;
const shoppingListQtyCol = 1;
const taobaoCartIdCol = 0;
const taobaoCartQtyCol = 4;
// --- End Configuration ---

// --- Function Definitions ---

/**
 * Reads a CSV file and aggregates parts by ID only, ignoring color.
 * @param {string} filePath Path to the CSV file.
 * @param {number} idColumnIndex Index of the column containing the Part ID.
 * @param {number} quantityColumnIndex Index of the column containing the Quantity.
 * @returns {Map<string, number>} A map where keys are Part IDs and values are total quantities.
 */
function readAndAggregateCsvByIdOnly(
  filePath,
  idColumnIndex,
  quantityColumnIndex
) {
  console.log(
    `Reading and aggregating quantities by ID only from: ${filePath}`
  );
  const content = fs.readFileSync(filePath);
  const records = parse(content, {
    columns: true,
    skip_empty_lines: true,
    trim: true,
    relax_column_count: true,
  });

  const partsMap = new Map();
  if (records.length === 0) {
    console.warn(`Warning: No data found in ${filePath}`);
    return partsMap;
  }

  const headers = Object.keys(records[0]);
  if (
    idColumnIndex >= headers.length ||
    quantityColumnIndex >= headers.length
  ) {
    throw new Error(
      `Invalid column index specified for ${filePath}. Max index: ${
        headers.length - 1
      }`
    );
  }
  const idHeader = headers[idColumnIndex];
  const quantityHeader = headers[quantityColumnIndex];

  for (const record of records) {
    const partId = record[idHeader]?.trim();
    const quantityStr = record[quantityHeader]?.trim();

    const quantityMatch = quantityStr?.match(/\d+/);
    const quantity = quantityMatch ? parseInt(quantityMatch[0], 10) : NaN;

    if (partId && partId.length > 0 && !isNaN(quantity) && quantity >= 0) {
      partsMap.set(partId, (partsMap.get(partId) || 0) + quantity);
    } else {
      // Optional: Warn about skipped rows if needed
      // if (!partId || isNaN(quantity)) {
      //    console.warn(`Skipping row in ${filePath} due to missing/invalid ID ('${partId}') or Quantity ('${quantityStr}'):`, record);
      // }
    }
  }
  console.log(
    `Aggregated ${partsMap.size} unique part IDs (ignoring color) from ${filePath}`
  );
  return partsMap;
}

// --- Main Execution ---
try {
  console.log('\n--- Running Part Comparison (Ignoring Color) ---');

  // Read shopping list (aggregate by ID only)
  const requiredParts = readAndAggregateCsvByIdOnly(
    shoppingListPath,
    shoppingListIdCol,
    shoppingListQtyCol
  );

  // Read Taobao cart (aggregate by ID only)
  const cartParts = readAndAggregateCsvByIdOnly(
    taobaoCartPath,
    taobaoCartIdCol,
    taobaoCartQtyCol
  );

  const missingParts = [];

  // Compare required parts against the cart based on Part ID only
  for (const [partId, requiredQty] of requiredParts.entries()) {
    const cartQty = cartParts.get(partId) || 0; // Look up using Part ID

    if (cartQty === 0) {
      // Part is completely missing from the cart
      missingParts.push({ partId, requiredQty });
    }
    // Ignore cases where the part exists in the cart, regardless of quantity
  }

  // --- Output Results ---
  console.log(`\n--- Comparison Report (Ignoring Color) ---`);

  console.log(`\n❌ Parts Missing from Cart (${missingParts.length}):`);
  if (missingParts.length > 0) {
    // Sort missing parts by ID for easier reading
    missingParts.sort((a, b) => a.partId.localeCompare(b.partId));
    missingParts.forEach((p) =>
      console.log(
        `  - Part ${p.partId}: Required quantity (any color) ${p.requiredQty}, Found 0 in cart`
      )
    );
  } else {
    console.log(
      '  (All required Part IDs were found in the cart, quantity/color not checked)'
    );
  }

  console.log(`\n--- End Report ---`);
  console.log(
    `\nNote: This comparison ignores color and only lists Part IDs completely absent from the cart.`
  );
} catch (error) {
  console.error('\n--- Error ---');
  console.error('An error occurred:');
  console.error(error.message);
  if (error.code === 'ENOENT') {
    console.error('Please ensure both CSV files exist at the specified paths:');
    console.error(`- Shopping List: ${shoppingListPath}`);
    console.error(`- Taobao Cart: ${taobaoCartPath}`);
  } else if (error.message.includes('csv-parse')) {
    console.error(
      'Failed to parse a CSV file. Check the file format, encoding (should be UTF-8), and ensure the header row is correct.'
    );
  } else {
    console.error('Stack Trace:', error.stack); // More detailed error for debugging
  }
  console.log('--- End Error ---');
}
