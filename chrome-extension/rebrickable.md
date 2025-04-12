# 项目背景

## 网址

`https://rebrickable.com/mocs/MOC-13349/Nico71/compact-tracked-loader/#parts`

## 单个零件卡片结构

```html
        <div class="text-center js-part-popup js-part-data" data-url="/parts/3708/summary/" data-part_id="23836" data-list_part_type="InvPart" data-list_part_id="1585720" data-can_edit="0" data-part_name="Technic Axle 12" data-part_cat_name="Technic Axles" data-color_id="0" data-color_name="Black" data-color_hsv="#001dd3 05131D" data-quantity="1" data-is_spare="0" data-price="2.7666606800000000">

          
          <div class="relative">
            <img class="img-responsive lazy-loaded" src="https://cdn.rebrickable.com/media/thumbs/parts/elements/370826.jpg/85x85p.jpg?1658325743.3637855" data-src="https://cdn.rebrickable.com/media/thumbs/parts/elements/370826.jpg/85x85p.jpg?1658325743.3637855" width="85" height="85" title="3708 Technic Axle 12
in Black
Technic Axles
(You do not have this part/color in your buildable parts collection)">
            
              
                <img class="overlay dark-0 img-responsive" src="https://rebrickable.com/static/img/overlays/ov_12.png?1692235612.5594056" width="85" height="85" title="3708 Technic Axle 12
in Black
Technic Axles
(You do not have this part/color in your buildable parts collection)">
              
            
          </div>

          
            <div class="part-text pt-3 ">
              <small class="trunc" title="1 x 3708"><b>1 x</b> 3708<font class="__Cici__translate__ __Cici_translate_similar_text_content__"><font class="__Cici_translate_origin_node__" style="display: none;"><b data-text-content="1 x">1 x</b> 3708</font> <font class="__Cici_translate_translated_inject_node__" style="display: inline-block;"><span>1 x 3708</span></font></font></small>
            </div>
            
              
                <div class="js-part-price" style="display: none;"><small>CN¥2.77</small></div>
              
            
          

        </div>
```


这是一个 rebrickable 网站页面中零件列表中的一个零件卡片，列表中有很多这样的商品卡片，请根据这个卡片的结构，生成一个获取所有零件卡片信息的 chrome 插件，chrome 插件会生成一个表格，表格中需要包含每个零件的编号、名称、颜色、数量、分类、图片。其中编号在 class 为 "text-center js-part-popup js-part-data" 的 div 标签 data-url 属性中，名称在 data-part_name 属性中，颜色在 data-color_name 属性中，数量在 data-quantity 属性中，分类在 data-part_cat_name 属性中，图片在该 div 下面的 div 标签下面的 img 标签中（class 为 "img-responsive lazy-loaded" 的 img 标签的 src 属性中）。

编号需要用正则表达式获取，正则表达式为：`/parts/(\d+)/summary/`，获取到的编号需要去掉前面的 `/parts/` 和后面的 `/summary/`

该 chrome 插件能够生成表格、预览生成的表格，并能够保存为 csv 文件，csv 名称为网址中的 MOC 编号 + 积木名称。

csv 名称为网址中的 MOC 编号，例如：

`https://rebrickable.com/mocs/MOC-13349/Nico71/compact-tracked-loader/#parts`

csv 名称为：MOC-13349_compact-tracked-loader.csv



