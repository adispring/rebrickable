document.addEventListener('DOMContentLoaded', () => {
  const extractBtn = document.getElementById('extractBtn');
  const saveBtn = document.getElementById('saveBtn');
  const previewContainer = document.getElementById('previewContainer');
  const tableContainer = document.getElementById('tableContainer');

  let partsData = [];

  extractBtn.addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true,
    });

    chrome.scripting.executeScript(
      {
        target: { tabId: tab.id },
        function: () => {
          return (
            document.querySelector(
              '.text-center.js-part-popup.js-part-data'
            ) !== null
          );
        },
      },
      async (results) => {
        if (results[0].result) {
          chrome.tabs.sendMessage(
            tab.id,
            { action: 'extractParts' },
            (response) => {
              if (response && response.parts) {
                partsData = response.parts;
                displayTable(partsData);
                previewContainer.style.display = 'block';
              }
            }
          );
        } else {
          alert('请在 Rebrickable 网站的零件列表页面使用此扩展');
        }
      }
    );
  });

  saveBtn.addEventListener('click', async () => {
    if (partsData.length === 0) return;

    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true,
    });
    const mocMatch = tab.url.match(/\/mocs\/(MOC-\d+)\/([^\/]+)\/([^\/]+)\//);
    const mocId = mocMatch ? mocMatch[1] : 'unknown';
    const modelName = mocMatch ? mocMatch[3].replace(/-/g, '_') : 'unknown';

    const csvContent = [
      ['零件编号', '零件名称', '零件分类', '颜色', '数量', '图片链接'].join(
        ','
      ),
      ...partsData.map((part) =>
        [
          part.partId,
          `"${part.partName}"`,
          `"${part.category}"`,
          `"${part.colorName}"`,
          part.quantity,
          part.imageUrl,
        ].join(',')
      ),
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `${mocId}_${modelName}.csv`);
    link.click();
  });

  function displayTable(parts) {
    const table = document.createElement('table');
    table.innerHTML = `
      <thead>
        <tr>
          <th>零件编号</th>
          <th>零件名称</th>
          <th>零件分类</th>
          <th>颜色</th>
          <th>数量</th>
          <th>图片</th>
        </tr>
      </thead>
      <tbody>
        ${parts
          .map(
            (part) => `
          <tr>
            <td>${part.partId}</td>
            <td>${part.partName}</td>
            <td>${part.category}</td>
            <td>${part.colorName}</td>
            <td>${part.quantity}</td>
            <td>
              ${
                part.imageUrl
                  ? `
                <img src="${part.imageUrl}" 
                     alt="${part.partName}" 
                     onerror="this.style.display='none'"
                     style="max-width: 50px; max-height: 50px;">
              `
                  : '无图片'
              }
            </td>
          </tr>
        `
          )
          .join('')}
      </tbody>
    `;

    tableContainer.innerHTML = '';
    tableContainer.appendChild(table);
  }
});
