from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent, Browser, BrowserConfig

load_dotenv()

import asyncio
import os

task = """
### 购物代理提示 - 淘宝在线商店购物

```csv
零件编号,零件名称,颜色,数量,图片链接
3708,"Technic Axle 12","Black",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/370826.jpg/85x85p.jpg?1658325743.3637855
3705,"Technic Axle 4","Black",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/370526.jpg/85x85p.jpg?1658325724.9877822
3706,"Technic Axle 6","Black",6,https://cdn.rebrickable.com/media/thumbs/parts/elements/370626.jpg/85x85p.jpg?1658325740.439785
59443,"Technic Axle Connector Smooth [with x Hole + Orientation]","Black",8,https://cdn.rebrickable.com/media/thumbs/parts/elements/4512363.jpg/85x85p.jpg?1658325740.463785
32039,"Technic Axle Connector with Axle Hole","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107081.jpg/85x85p.jpg?1658325748.9957864
18651,"Technic Axle Pin 3L with Friction Ridges Lengthwise and 2L Axle","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/6089119.jpg/85x85p.jpg?1658325740.483785
32013,"Technic Axle and Pin Connector Angled #1","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107085.jpg/85x85p.jpg?1658325740.8557851
32034,"Technic Axle and Pin Connector Angled #2 - 180°","Black",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107783.jpg/85x85p.jpg?1658325740.867785
32016,"Technic Axle and Pin Connector Angled #3 - 157.5°","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107082.jpg/85x85p.jpg?1658325738.4117846
32192,"Technic Axle and Pin Connector Angled #4 - 135°","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4121610.jpg/85x85p.jpg?1658325748.9957864
32015,"Technic Axle and Pin Connector Angled #5 - 112.5°","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107084.jpg/85x85p.jpg?1658325791.6197937
6536,"Technic Axle and Pin Connector Perpendicular","Black",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4173668.jpg/85x85p.jpg?1658325738.3077846
32184,"Technic Axle and Pin Connector Perpendicular 3L with Centre Pin Hole","Black",5,https://cdn.rebrickable.com/media/thumbs/parts/elements/4121667.jpg/85x85p.jpg?1658325740.8917851
32291,"Technic Axle and Pin Connector Perpendicular Double","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4140430.jpg/85x85p.jpg?1658325751.3277867
41239,"Technic Beam 1 x 13 Thick","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4164422.jpg/85x85p.jpg?1658325740.919785
32278,"Technic Beam 1 x 15 Thick","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4128603.jpg/85x85p.jpg?1658325740.935785
60483,"Technic Beam 1 x 2 Thick with Pin Hole and Axle Hole","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4515185.jpg/85x85p.jpg?1658325740.935785
41677,"Technic Beam 1 x 2 Thin","Black",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4164133.jpg/85x85p.jpg?1658325740.935785
6632,"Technic Beam 1 x 3 Thin","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107828.jpg/85x85p.jpg?1658325741.395785
32449,"Technic Beam 1 x 4 Thin","Black",7,https://cdn.rebrickable.com/media/thumbs/parts/elements/4142236.jpg/85x85p.jpg?1658325741.395785
32524,"Technic Beam 1 x 7 Thick","Black",5,https://cdn.rebrickable.com/media/thumbs/parts/elements/4155458.jpg/85x85p.jpg?1658325741.4117851
40490,"Technic Beam 1 x 9 Thick","Black",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4154767.jpg/85x85p.jpg?1658325741.435785
32140,"Technic Beam 2 x 4 L-Shape Thick","Black",5,https://cdn.rebrickable.com/media/thumbs/parts/elements/4120017.jpg/85x85p.jpg?1658325741.4437852
33299a,"Technic Beam 3 x 0.5 Liftarm with Boss and Pin / Crank","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4156980.jpg/85x85p.jpg?1658325755.3877876
60484,"Technic Beam 3 x 3 T-Shape Thick","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4535771.jpg/85x85p.jpg?1740872079.084931
32526,"Technic Beam 3 x 5 L-Shape Thick","Black",6,https://cdn.rebrickable.com/media/thumbs/parts/elements/4142823.jpg/85x85p.jpg?1658325741.451785
32000,"Technic Brick 1 x 2 [2 Pin Holes]","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/3200026.jpg/85x85p.jpg?1658325756.3397877
2951,"Technic Digger Bucket 8 x 10","Black",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4288259.jpg/85x85p.jpg?1658325794.319794
32270,"Technic Gear 12 Tooth Double Bevel","Black",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4177431.jpg/85x85p.jpg?1658325741.4437852
15379,"Technic Link Tread with Beveled Edge","Black",80,https://cdn.rebrickable.com/media/thumbs/parts/elements/6047885.jpg/85x85p.jpg?1658325795.1277943
87082,"Technic Pin Connector Hub with 2 Pins with Friction Ridges Lengthwise [Big Squared Pin Holes]","Black",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4560174.jpg/85x85p.jpg?1658325741.471785
87408,"Technic Pin Connector Toggle Joint Smooth Double with Axle and Pin Holes","Black",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4558692.jpg/85x85p.jpg?1658325741.4677851
32054,"Technic Pin Long with Friction Ridges Lengthwise and Stop Bush [3 Lateral Holes, Big Pin Hole]","Black",6,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107742.jpg/85x85p.jpg?1658325741.4797852
2780,"Technic Pin with Friction Ridges Lengthwise and Center Slots","Black",46,https://cdn.rebrickable.com/media/thumbs/parts/elements/4121715.jpg/85x85p.jpg?1658325730.5597832
43093,"Technic Axle Pin with Friction Ridges Lengthwise","Blue",32,https://cdn.rebrickable.com/media/thumbs/parts/elements/4189110.jpg/85x85p.jpg?1740872078.3089159
6558,"Technic Pin Long with Friction Ridges Lengthwise, 2 Center Slots","Blue",25,https://cdn.rebrickable.com/media/thumbs/parts/elements/4514553.jpg/85x85p.jpg?1658325738.3957846
87083,"Technic Axle 4 with Stop","Dark Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4560177.jpg/85x85p.jpg?1658325733.6797838
59426,"Technic Axle 5.5 with Stop [Rounded Short End]","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4508553.jpg/85x85p.jpg?1658325742.9317853
59443,"Technic Axle Connector Smooth [with x Hole + Orientation]","Dark Bluish Gray",3,https://cdn.rebrickable.com/media/thumbs/parts/elements/4516546.jpg/85x85p.jpg?1658325734.2717838
11214,"Technic Axle Pin 3L with Friction Ridges Lengthwise and 1L Axle","Dark Bluish Gray",11,https://cdn.rebrickable.com/media/thumbs/parts/elements/6015356.jpg/85x85p.jpg?1658325741.8317852
61904,"Technic Axle and Pin Connector Block 4 x 3 x 2 1/2 [Linear Actuator Holder]","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4528038.jpg/85x85p.jpg?1658325741.8357852
6536,"Technic Axle and Pin Connector Perpendicular","Dark Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210851.jpg/85x85p.jpg?1658325742.9797854
32278,"Technic Beam 1 x 15 Thick","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210687.jpg/85x85p.jpg?1658325734.2717838
60483,"Technic Beam 1 x 2 Thick with Pin Hole and Axle Hole","Dark Bluish Gray",5,https://cdn.rebrickable.com/media/thumbs/parts/elements/4515183.jpg/85x85p.jpg?1658325795.1757941
41677,"Technic Beam 1 x 2 Thin","Dark Bluish Gray",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210980.jpg/85x85p.jpg?1658325847.347803
6632,"Technic Beam 1 x 3 Thin","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4223767.jpg/85x85p.jpg?1658325795.287794
32449,"Technic Beam 1 x 4 Thin","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210749.jpg/85x85p.jpg?1658325839.8958018
32316,"Technic Beam 1 x 5 Thick","Dark Bluish Gray",3,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210686.jpg/85x85p.jpg?1658325787.3677928
32524,"Technic Beam 1 x 7 Thick","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210752.jpg/85x85p.jpg?1658325787.3717928
6629,"Technic Beam 1 x 9 Bent (6 - 4) Thick","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210638.jpg/85x85p.jpg?1658325787.3877928
32271,"Technic Beam 1 x 9 Bent (7 - 3) Thick","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210673.jpg/85x85p.jpg?1682131925.7718782
32056,"Technic Beam 3 x 3 L-Shape Thin","Dark Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210659.jpg/85x85p.jpg?1658325795.3117943
60484,"Technic Beam 3 x 3 T-Shape Thick","Dark Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4535773.jpg/85x85p.jpg?1740890054.9966853
3648b,"Technic Gear 24 Tooth [New Style with Single Axle Hole]","Dark Bluish Gray",8,https://cdn.rebrickable.com/media/thumbs/parts/elements/4514558.jpg/85x85p.jpg?1658325738.3517847
3647,"Technic Gear 8 Tooth","Dark Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4514559.jpg/85x85p.jpg?1658325839.5878017
32557,"Technic Pin Connector Perpendicular Long","Dark Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4210756.jpg/85x85p.jpg?1658326889.663922
6587,"Technic Axle 3 with Stud","Dark Tan",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4566927.jpg/85x85p.jpg?1658325782.483792
15462,"Technic Axle 5 with Stop","Dark Tan",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/6055631.jpg/85x85p.jpg?1658325787.4077928
84599,"Battery Box, Power Functions, with Dark Bluish Gray Bottom [Rechargeable]","Light Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/6163683.jpg/85x85p.jpg?1658326006.5798163
58122,"Control Unit, IR, Power Functions, with Dark Bluish Gray Bottom","Light Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4506079.jpg/85x85p.jpg?1658325796.7157946
58120,"Motor, Medium, Power Functions, 3 x 6 x 3 with Dark Bluish Gray Bottom and 20cm Wire","Light Bluish Gray",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4506083.jpg/85x85p.jpg?1658325779.2517915
2817,"Plate Special 2 x 2 with 2 Pin Holes","Light Bluish Gray",5,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211376.jpg/85x85p.jpg?1658325739.8957849
58123b,"Receiver Unit, IR, Power Functions, with V2 Print","Light Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/6034993.jpg/85x85p.jpg?1658325903.5758092
4519,"Technic Axle 3","Light Bluish Gray",14,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211815.jpg/85x85p.jpg?1658325738.3957846
32073,"Technic Axle 5","Light Bluish Gray",3,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211639.jpg/85x85p.jpg?1658325742.1397853
44294,"Technic Axle 7","Light Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211805.jpg/85x85p.jpg?1658325738.4277847
60485,"Technic Axle 9","Light Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4535768.jpg/85x85p.jpg?1658325742.1397853
32523,"Technic Beam 1 x 3 Thick","Light Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211655.jpg/85x85p.jpg?1658325893.0758085
32063,"Technic Beam 1 x 6 Thin","Light Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211586.jpg/85x85p.jpg?1658325818.039798
3713,"Technic Bush","Light Bluish Gray",3,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211622.jpg/85x85p.jpg?1658325742.1277852
32123b,"Technic Bush 1/2 Smooth with Axle Hole Semi-Reduced","Light Bluish Gray",3,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211573.jpg/85x85p.jpg?1740872093.7452123
92693,"Technic Linear Actuator Mini with Dark Bluish Gray Head and Orange Axle","Light Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4612100.jpg/85x85p.jpg?1658325742.1557853
61927b,"Technic Linear Actuator with Dark Bluish Gray Ends [Improved Version]","Light Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4638507.jpg/85x85p.jpg?1658325995.0678153
4274,"Technic Pin 1/2","Light Bluish Gray",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211483.jpg/85x85p.jpg?1658325742.3917854
62462,"Technic Pin Connector Round [Slotted]","Light Bluish Gray",3,https://cdn.rebrickable.com/media/thumbs/parts/elements/4526985.jpg/85x85p.jpg?1658325834.8798008
32054,"Technic Pin Long with Friction Ridges Lengthwise and Stop Bush [3 Lateral Holes, Big Pin Hole]","Light Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211865.jpg/85x85p.jpg?1658325804.703796
3673,"Technic Pin without Friction Ridges Lengthwise","Light Bluish Gray",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4211807.jpg/85x85p.jpg?1658325739.5717847
61903,"Technic Universal Joint 3L [Complete Assembly]","Light Bluish Gray",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4525904.jpg/85x85p.jpg?1658325742.4197853
32062,"Technic Axle 2 Notched","Red",18,https://cdn.rebrickable.com/media/thumbs/parts/elements/4142865.jpg/85x85p.jpg?1658325711.4477801
99008,"Technic Axle 4 with Centre Stop","Tan",4,https://cdn.rebrickable.com/media/thumbs/parts/elements/4666999.jpg/85x85p.jpg?1658325782.499792
3749,"Technic Axle Pin without Friction Ridges Lengthwise","Tan",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4133591.jpg/85x85p.jpg?1740872186.0189943
6589,"Technic Gear 12 Tooth Bevel","Tan",6,https://cdn.rebrickable.com/media/thumbs/parts/elements/4514556.jpg/85x85p.jpg?1658325752.099787
32198,"Technic Gear 20 Tooth Bevel","Tan",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4514557.jpg/85x85p.jpg?1658325752.0717869
32002,"Technic Pin 3/4","Tan",5,https://cdn.rebrickable.com/media/thumbs/parts/elements/6013938.jpg/85x85p.jpg?1658325809.9517968
32556,"Technic Pin Long without Friction Ridges","Tan",2,https://cdn.rebrickable.com/media/thumbs/parts/photos/19/32556-19-22727d9e-2cd4-4ab9-8a17-a619c8ae7eb4.jpg/85x85p.jpg?1739186277.0000222
3023,"Plate 1 x 2","Trans-Clear",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4167842.jpg/85x85p.jpg?1658325837.8318014
6141,"Plate Round 1 x 1 with Solid Stud","Trans-Red",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/3005741.jpg/85x85p.jpg?1710483508.8352046
3460,"Plate 1 x 8","Yellow",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/346024.jpg/85x85p.jpg?1658325814.1597974
6536,"Technic Axle and Pin Connector Perpendicular","Yellow",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107078.jpg/85x85p.jpg?1658325819.5277984
32009,"Technic Beam 1 x 11.5 Double Bent Thick","Yellow",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107079.jpg/85x85p.jpg?1709726404.932607
32523,"Technic Beam 1 x 3 Thick","Yellow",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/4153707.jpg/85x85p.jpg?1658325972.1358137
32316,"Technic Beam 1 x 5 Thick","Yellow",5,https://cdn.rebrickable.com/media/thumbs/parts/elements/4128590.jpg/85x85p.jpg?1740872312.8934453
32017,"Technic Beam 1 x 5 Thin","Yellow",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4107080.jpg/85x85p.jpg?1658325830.6838002
32524,"Technic Beam 1 x 7 Thick","Yellow",3,https://cdn.rebrickable.com/media/thumbs/parts/elements/4495934.jpg/85x85p.jpg?1658325830.6398003
32065,"Technic Beam 1 x 7 Thin","Yellow",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4114672.jpg/85x85p.jpg?1658326510.21587
40490,"Technic Beam 1 x 9 Thick","Yellow",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4187136.jpg/85x85p.jpg?1658325902.567809
32140,"Technic Beam 2 x 4 L-Shape Thick","Yellow",2,https://cdn.rebrickable.com/media/thumbs/parts/elements/4141628.jpg/85x85p.jpg?1658325825.0717993
3701,"Technic Brick 1 x 4 [3 Pin Holes]","Yellow",1,https://cdn.rebrickable.com/media/thumbs/parts/elements/370124.jpg/85x85p.jpg?1658325817.0917978
```

**目标：**
访问[淘宝在线商店 的 MOC积木大王 商家](https://shop106503467.taobao.com/?spm=pc_detail.29232929/evo365560b447259.shop_block.dshopinfo.18fa7dd61AXcVl)，搜索所需的乐高积木零件，按照型号、颜色 和 数量 将它们添加到购物车。

**重要提示：**
- 确保每件商品都不要购买超过所需数量。
- 搜索后，点击 "加入购物车" 按钮可以将商品添加到购物车。

**具体步骤：**
---

### 第1步：获取零件清单
- 要买的零件在上面的 csv 中，提取型号、颜色和数量。
- 将清单打印出来打印出来


### 第2步：访问网站
- 打开[淘宝在线商店](https://shop106503467.taobao.com/?spm=pc_detail.29232929/evo365560b447259.shop_block.dshopinfo.18fa7dd61AXcVl)。
- 需要等待用户扫描二维码登录

### 第3步：将商品添加到购物车

#### 添加商品到购物车的步骤：
- 对于每个零件型号，打开[淘宝在线商店](https://shop106503467.taobao.com/?spm=pc_detail.29232929/evo365560b447259.shop_block.dshopinfo.18fa7dd61AXcVl)。
- 在搜索框中输入零件型号，点击 “搜本店”。
- 在搜索结果中，找到与型号匹配的产品。
- 如果找到匹配的产品，进入产品页，找到与颜色匹配的产品。
- 检查库存数量是否足够。
- 点击 "+" 按钮可以增加所需的数量，点击 "-" 按钮可以减少所需的数量，也可以直接输入所需的数量。
- 有的产品可能是按单个卖，有的产品可能按10个一组卖。
- 如果库存数量不足，记录下来，以便稍后手动处理。
- 点击 "加入购物车" 按钮将其添加到购物车。
- 确保每件商品都不要购买超过所需数量。
- 如果没有找到匹配的产品，请记录下来，以便稍后手动处理。

---

**重要提示：** 确保整个过程的效率和准确性。"""

# config = BrowserConfig(
#     chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# )

browser = Browser()

llm = ChatOpenAI(
    model="gpt-4o-2024-11-20",
    base_url=os.getenv("OPENAI_ENDPOINT"),
    api_key=os.getenv("OPENAI_API_KEY")
)

agent = Agent(
	task=task,
	llm=llm,
	browser=browser,
)


async def main():
	await agent.run()
	input('Press Enter to close the browser...')
	await browser.close()


if __name__ == '__main__':
	asyncio.run(main())