document.addEventListener('DOMContentLoaded', () => {
  const extractBtn = document.getElementById('extractBtn');
  const saveBtn = document.getElementById('saveBtn');
  const previewContainer = document.getElementById('previewContainer');
  const tableContainer = document.getElementById('tableContainer');
  const statsContainer = document.getElementById('statsContainer');
  const currentTimeElement = document.getElementById('currentTime');
  const fileNameElement = document.getElementById('fileName');
  const totalPriceElement = document.getElementById('totalPrice');

  let productsData = [];
  let fileName = '';

  // 更新当前时间和文件名
  function updateTimeAndFileName() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    const formattedTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    const formattedFileName = `淘宝-${year}-${month}-${day}-${hours}-${minutes}-${seconds}.csv`;

    currentTimeElement.textContent = `当前时间: ${formattedTime}`;
    fileNameElement.textContent = `文件名: ${formattedFileName}`;
    fileName = formattedFileName;
  }

  // 初始化时更新时间和文件名
  updateTimeAndFileName();

  // 每秒更新一次时间和文件名
  setInterval(updateTimeAndFileName, 1000);

  extractBtn.addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true,
    });

    // 检查当前页面是否为淘宝购物车页面
    if (!tab.url.includes('taobao.com/cart')) {
      alert('请在淘宝购物车页面使用此扩展');
      return;
    }

    chrome.tabs.sendMessage(
      tab.id,
      { action: 'extractProductInfo' },
      (response) => {
        if (response && response.products) {
          productsData = response.products;
          totalPriceElement.textContent = response.totalPrice;
          displayTable(productsData);
          previewContainer.style.display = 'block';
        } else {
          alert('无法获取购物车数据，请确保您已登录并且购物车中有商品');
        }
      }
    );
  });

  saveBtn.addEventListener('click', () => {
    if (productsData.length === 0) {
      alert('没有可保存的数据');
      return;
    }

    // 更新文件名（确保获取最新时间戳）
    updateTimeAndFileName();

    const csvContent = [
      ['编号', '商品名称', '颜色', '单价', '数量', '小计', '图片链接'].join(
        ','
      ),
      ...productsData.map((product) =>
        [
          product.id,
          `"${product.name.replace(/"/g, '""')}"`,
          `"${product.color.replace(/"/g, '""')}"`,
          product.price,
          product.quantity,
          product.subtotal,
          product.image,
        ].join(',')
      ),
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', fileName);
    link.click();
  });

  function displayTable(products) {
    if (products.length === 0) {
      tableContainer.innerHTML = '<p>没有找到乐高商品</p>';
      return;
    }

    const table = document.createElement('table');
    table.innerHTML = `
      <thead>
        <tr>
          <th>编号</th>
          <th>商品名称</th>
          <th>颜色</th>
          <th>单价(￥)</th>
          <th>数量</th>
          <th>小计(￥)</th>
          <th>图片</th>
        </tr>
      </thead>
      <tbody>
        ${products
          .map(
            (product) => `
          <tr>
            <td>${product.id}</td>
            <td>${product.name}</td>
            <td>${product.color}</td>
            <td>${product.price.toFixed(2)}</td>
            <td>${product.quantity}</td>
            <td>${product.subtotal}</td>
            <td>
              ${
                product.image
                  ? `
                <img src="${product.image}" 
                     alt="${product.name}" 
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
