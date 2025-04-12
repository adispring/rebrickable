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
