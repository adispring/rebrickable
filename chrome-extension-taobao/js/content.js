function extractPartsInfo() {
  const parts = [];
  const partElements = document.querySelectorAll(
    '.text-center.js-part-popup.js-part-data'
  );

  partElements.forEach((element) => {
    try {
      const url = element.getAttribute('data-url');
      const partIdMatch = url.match(/\/parts\/([a-zA-Z0-9]+)\/summary/);
      if (!partIdMatch) {
        console.warn('无法匹配零件编号:', url);
        return;
      }

      const partId = partIdMatch[1];
      const partName = element.getAttribute('data-part_name');
      const colorName = element.getAttribute('data-color_name');
      const quantity = element.getAttribute('data-quantity');
      const category = element.getAttribute('data-part_cat_name');

      // 获取图片元素
      const imgElement = element.querySelector('.img-responsive.lazy-loaded');
      let imageUrl = '';
      if (imgElement) {
        // 使用 data-src 属性，它通常包含原始图片 URL
        imageUrl =
          imgElement.getAttribute('data-src') || imgElement.getAttribute('src');
      }

      parts.push({
        partId,
        partName,
        category,
        colorName,
        quantity,
        imageUrl,
      });
    } catch (error) {
      console.error('处理零件信息时出错:', error);
    }
  });

  return parts;
}

// 监听来自 popup 的消息
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'extractParts') {
    const parts = extractPartsInfo();
    sendResponse({ parts });
  }
  return true;
});

// 提取淘宝购物车中的商品信息
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'extractProductInfo') {
    const productInfo = extractProductInfo();
    sendResponse(productInfo);
  }
});

// 提取商品信息
function extractProductInfo() {
  // 获取所有商品卡片
  const productCards = document.querySelectorAll('.trade-cart-item-info');
  const products = [];
  let totalPrice = 0;

  productCards.forEach((card) => {
    try {
      // 获取标题信息
      const titleElem = card.querySelector(
        '.trade-cart-item-detail a.title--dsuLK9IN'
      );
      const title = titleElem?.title || titleElem?.textContent || '';

      // 使用正则表达式提取编号，允许"适用乐高"和数字之间有空格
      const idMatch = title.match(/适用乐高\s*(\d+)/);
      const id = idMatch ? idMatch[1] : '';

      // 如果没有找到编号，说明不是乐高商品，跳过
      if (!id) return;

      // 获取颜色信息
      const colorElem = card.querySelector(
        '.trade-cart-item-sku-old .label--T4deixnF'
      );
      const colorText = colorElem?.textContent || '';
      const color = colorText.replace('颜色分类：', '').trim();

      // 获取价格信息
      const priceIntElem = card.querySelector(
        '.trade-cart-item-price .trade-price-integer'
      );
      const priceDecimalElem = card.querySelector(
        '.trade-cart-item-price .trade-price-decimal'
      );
      const priceInt = priceIntElem?.textContent || '0';
      const priceDecimal = priceDecimalElem?.textContent || '00';
      const price = parseFloat(priceInt + '.' + priceDecimal);

      // 获取数量信息
      const quantityElem = card.querySelector(
        '.trade-cart-item-quantity input'
      );
      const quantity = parseInt(quantityElem?.value || '0');

      // 获取图片信息
      const imageElem = card.querySelector('.trade-cart-item-image img');
      const imageSrc = imageElem?.src || '';
      // 确保图片URL是完整的
      const fullImageSrc = imageSrc.startsWith('//')
        ? 'https:' + imageSrc
        : imageSrc;

      // 计算小计
      const subtotal = price * quantity;
      totalPrice += subtotal;

      // 添加商品信息
      products.push({
        id: id,
        name: title,
        color: color,
        price: price,
        quantity: quantity,
        image: fullImageSrc,
        subtotal: subtotal.toFixed(2),
      });
    } catch (e) {
      console.error('提取商品信息时出错:', e);
    }
  });

  return {
    products: products,
    totalPrice: totalPrice.toFixed(2),
  };
}
