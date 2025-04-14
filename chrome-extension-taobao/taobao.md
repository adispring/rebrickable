# 项目背景

## 网址

`https://cart.taobao.com/cart.htm?spm=a21bo.jianhua/a.1997525049.1.5af92a89Ymh6k6&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739`

## 单个零件卡片结构

```html
<div class="trade-cart-item-info cartItemInfo--dgMKAZ9u">
  <div class="cartItemInfoContainer--wrOMc6CC">
    <div class="trade-cart-item-status cartStatus--ybsdrE6_">
      <label class="ant-checkbox-wrapper">
        <span class="ant-checkbox">
          <input class="ant-checkbox-input" type="checkbox">
          <span class="ant-checkbox-inner"></span>
        </span>
      </label>
    </div>
    <div class="trade-cart-item-image cartImage--DFDRCC0D" data-spm="item">
      <a class="imageContainer--hftQeZJa" target="_blank" href="https://item.taobao.com/item.htm?id=577319488509&amp;from=cart&amp;skuId=5097682550369" data-spm="d577319488509">
        <img class="image--MC0kGGgi" src="//gw.alicdn.com/imgextra/i1/733216778/O1CN01ih92vJ1zwNLAmDvOi_!!733216778.jpg">
        <div class="imageMask--RmmOLZ9F"></div>
      </a>
    </div>
    <div class="trade-cart-item-d-p-q-container cartItemDPQContainer--S7yQtAoY">
      <div class="trade-cart-item-detail cartDetail--cxJIGPoh" data-spm="item">
        <div class="rightWrapper--dsxd67c_">
          <a class="title--dsuLK9IN" title="适用乐高3701国产积木科技零配散件 370126 黑色 1x4带3孔砖" target="_blank" href="https://item.taobao.com/item.htm?id=577319488509&amp;from=cart&amp;skuId=5097682550369" data-spm="d577319488509">适用乐高3701国产积木科技零配散件 370126 黑色 1x4带3孔砖</a>
          <div class="benefitWrapper--OQuVuUjS">
            <div class="benefitListWrapper--KFysO6cH payMethodTag--pmv0fVbB">
              <div class="benefitTag--JY1RPdSK">信用卡支付</div>
            </div>
            <div>&nbsp;</div>
          </div>
          <div class="benefitWrapper--OQuVuUjS">
            <div class="benefitListWrapper--KFysO6cH">
              <div class="benefitTag--JY1RPdSK ">7天无理由退货</div>
              <div class="benefitTag--JY1RPdSK ">极速退款</div>
            </div>
            <div>&nbsp;</div>
          </div>
        </div>
      </div>
      <div class="trade-cart-item-sku-old sku--vewlsl6e">
        <div class="content--nFZ3Sgmr  ">
          <div class="label--T4deixnF">颜色分类：黄色</div>
        </div>
      </div>
      <div class="trade-cart-item-p-q-container cartItemPQContainer--_bt9FLmy">
        <div class="trade-cart-item-price cartPriceInfo--KkqVW5lA ">
          <div class="trade-price-container type-of-12-14B-16B  " style="color: rgb(255, 80, 0);">
            <span class="trade-price-symbol ">￥</span>
            <span class="trade-price-integer ">0</span>
            <span class="trade-price-point ">.</span>
            <span class="trade-price-decimal ">13</span>
          </div>
        </div>
        <div class="trade-cart-item-quantity cartQuantity--Z6Q5IngB">
          <div class="quantityWrapper--m1OWRRbC" title="数量1">
            <div class="minusWrapper--Mw5Kus1n minusWrapperDisabled--LAhtK4MO" aria-label="减少按钮">
              <svg viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3619" width="20" height="20">
                <path d="M716.8 467.2a44.8 44.8 0 1 1 0 89.6H307.2a44.8 44.8 0 1 1 0-89.6h409.6z" fill="#CCCCCC" p-id="3620"></path>
              </svg>
            </div>
            <input aria-label="数量1" class="ant-input inputWrapper--jtTJwDAk" type="text" value="1">
            <div class="addWrapper--B6P0H0ft " aria-label="增加按钮">
              <svg viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3764" width="20" height="20">
                <path d="M512 262.4c24.7296 0 44.8 20.0704 44.8 44.8v160H716.8c22.8352 0 41.6768 17.1008 44.4416 39.168l0.3584 5.632a44.8 44.8 0 0 1-44.8 44.8h-160V716.8a44.8 44.8 0 0 1-39.168 44.4416l-5.632 0.3584A44.8 44.8 0 0 1 467.2 716.8v-160H307.2a44.8 44.8 0 0 1-44.4416-39.168L262.4 512c0-24.7296 20.0704-44.8 44.8-44.8h160V307.2c0-22.8352 17.1008-41.6768 39.168-44.4416l5.632-0.3584z" fill="#1F1F1F" p-id="3765"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="trade-cart-item-operation cartOperation--K9S4hQC3">
      <div class="cartOperationItem--a7tKcvAI">移入收藏</div>
      <div class="cartOperationItem--a7tKcvAI">删除</div>
    </div>
  </div>
</div>
```

这是一个淘宝网站购物车页面中商品列表中的一个商品卡片，列表中有很多这样的商品卡片，请根据这个卡片的结构，生成一个获取商品列表中所有商品卡片信息的 chrome 插件，chrome 插件会生成一个表格，表格中需要包含每个商品的编号、名称、颜色、单价、数量、图片。

- 其中每个商品卡片容器为 class 为 "trade-cart-item-info" 的 div 标签；
- 编号在 class 为 "trade-cart-item-detail" 的 div 标签中的 a 标签的 title 属性中，需要用正则匹配出编号，编号为 `适用乐高` 后面的数字，如果匹配不到编号，则该商品为非乐高商品，不进行记录；
- 名称在 class 为 "trade-cart-item-detail" 的 div 标签中的 a 标签的 title 属性中；
- 颜色在 class 为 "trade-cart-item-sku-old" 的 div 标签中的 以 "label--" 开头的 div 标签内容中；
- 单价在 class 为 "trade-cart-item-price" 的 div 标签中的 div 标签中的 span 标签的内容中；
- 数量在 class 为 "trade-cart-item-quantity" 的 div 标签中的 input 标签的 value 属性中；
- 图片在该 div 下面的 div 标签下面的 img 标签中（class 为 "img-responsive lazy-loaded" 的 img 标签的 src 属性中）。

该 chrome 插件能够生成表格、预览生成的表格，并能够保存为 csv 文件，csv 名称为 “淘宝”-当前时间。例如：

csv 名称为：淘宝-2025-04-13-10-00-00.csv

预览 popup 页面，需要显示当前时间，以及当前时间对应的 csv 文件名，以及一个按钮，点击按钮后，生成 csv 文件，并保存为 csv 文件，csv 文件名称为 “淘宝”-当前时间。

popup 页面中还要展示所有商品的总价，总价为单价乘以数量，总价保留两位小数。
