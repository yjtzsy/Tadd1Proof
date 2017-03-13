# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 15:51:28 2017
一个实战策略的简单量化测试
看前一日股票收盘价、成交额以及换手率对今日股价的影响
@author: Administrator
"""
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn import datasets, linear_model
import sys

from WindPy import *
from datetime import *
w.start()


#load data
datelist = []
datelistJan = []
datelistFeb = []
dateJan = 20170101
dateFeb = 20170201
for i in range(31):
    datelistJan.append(dateJan)
    dateJan += 1
    
for i in range(28):
    datelistFeb.append(dateFeb)
    dateFeb += 1
    
datelistJan.extend(datelistFeb)
datelist = datelistJan


class strategeOne():
    def __init__(self, datelist):
        self.datelist = datelist
     
    
    def get_reward(self,y_true, y_fit):
        R2 = 1 - np.sum((y_true - y_fit)**2) / np.sum((y_true - np.mean(y_true))**2)
        R = np.sign(R2) * np.sqrt(abs(R2))
        return(R)

    
    def summary(self):
        theta = []
        R = []
        for i in range(len(self.datelist)):
            print(i)
            date = self.datelist[i]
            strdate = str(date) 
            dateString = "tradeDate="+strdate+";priceAdj=U;cycle=D"
            #"tradeDate=20170227;priceAdj=U;cycle=D"
    
            data = w.wss("600000.SH,600004.SH,600006.SH,600007.SH,600008.SH,600009.SH,600010.SH,600011.SH,600012.SH,600015.SH,600016.SH,600017.SH,600018.SH,600019.SH,600020.SH,600021.SH,600022.SH,600023.SH,600026.SH,600027.SH,600028.SH,600029.SH,600030.SH,600031.SH,600033.SH,600035.SH,600036.SH,600037.SH,600038.SH,600039.SH,600048.SH,600050.SH,600051.SH,600052.SH,600053.SH,600054.SH,600055.SH,600056.SH,600057.SH,600058.SH,600059.SH,600060.SH,600061.SH,600062.SH,600063.SH,600064.SH,600066.SH,600067.SH,600068.SH,600069.SH,600070.SH,600071.SH,600072.SH,600073.SH,600074.SH,600075.SH,600076.SH,600077.SH,600078.SH,600079.SH,600080.SH,600081.SH,600082.SH,600083.SH,600084.SH,600085.SH,600086.SH,600088.SH,600089.SH,600090.SH,600091.SH,600093.SH,600094.SH,600095.SH,600096.SH,600097.SH,600098.SH,600099.SH,600100.SH,600101.SH,600103.SH,600104.SH,600105.SH,600106.SH,600107.SH,600108.SH,600109.SH,600110.SH,600111.SH,600112.SH,600113.SH,600114.SH,600115.SH,600116.SH,600117.SH,600118.SH,600119.SH,600120.SH,600121.SH,600122.SH,600123.SH,600125.SH,600126.SH,600127.SH,600128.SH,600129.SH,600130.SH,600131.SH,600132.SH,600133.SH,600135.SH,600136.SH,600137.SH,600138.SH,600139.SH,600141.SH,600143.SH,600145.SH,600146.SH,600148.SH,600149.SH,600150.SH,600151.SH,600152.SH,600153.SH,600155.SH,600156.SH,600157.SH,600158.SH,600159.SH,600160.SH,600161.SH,600162.SH,600163.SH,600165.SH,600166.SH,600167.SH,600168.SH,600169.SH,600170.SH,600171.SH,600172.SH,600173.SH,600175.SH,600176.SH,600177.SH,600178.SH,600179.SH,600180.SH,600182.SH,600183.SH,600184.SH,600185.SH,600186.SH,600187.SH,600188.SH,600189.SH,600190.SH,600191.SH,600192.SH,600193.SH,600195.SH,600196.SH,600197.SH,600198.SH,600199.SH,600200.SH,600201.SH,600202.SH,600203.SH,600206.SH,600207.SH,600208.SH,600209.SH,600210.SH,600211.SH,600212.SH,600213.SH,600215.SH,600216.SH,600217.SH,600218.SH,600219.SH,600220.SH,600221.SH,600222.SH,600223.SH,600225.SH,600226.SH,600227.SH,600228.SH,600229.SH,600230.SH,600231.SH,600232.SH,600233.SH,600234.SH,600235.SH,600236.SH,600237.SH,600238.SH,600239.SH,600240.SH,600241.SH,600242.SH,600243.SH,600246.SH,600247.SH,600248.SH,600249.SH,600250.SH,600251.SH,600252.SH,600255.SH,600256.SH,600257.SH,600258.SH,600259.SH,600260.SH,600261.SH,600262.SH,600265.SH,600266.SH,600267.SH,600268.SH,600269.SH,600270.SH,600271.SH,600272.SH,600273.SH,600275.SH,600276.SH,600277.SH,600278.SH,600279.SH,600280.SH,600281.SH,600282.SH,600283.SH,600284.SH,600285.SH,600287.SH,600288.SH,600289.SH,600290.SH,600291.SH,600292.SH,600293.SH,600295.SH,600297.SH,600298.SH,600299.SH,600300.SH,600301.SH,600302.SH,600303.SH,600305.SH,600306.SH,600307.SH,600308.SH,600309.SH,600310.SH,600311.SH,600312.SH,600313.SH,600315.SH,600316.SH,600317.SH,600318.SH,600319.SH,600320.SH,600321.SH,600322.SH,600323.SH,600325.SH,600326.SH,600327.SH,600328.SH,600329.SH,600330.SH,600331.SH,600332.SH,600333.SH,600335.SH,600336.SH,600337.SH,600338.SH,600339.SH,600340.SH,600343.SH,600345.SH,600346.SH,600348.SH,600350.SH,600351.SH,600352.SH,600353.SH,600354.SH,600355.SH,600356.SH,600358.SH,600359.SH,600360.SH,600361.SH,600362.SH,600363.SH,600365.SH,600366.SH,600367.SH,600368.SH,600369.SH,600370.SH,600371.SH,600372.SH,600373.SH,600375.SH,600376.SH,600377.SH,600378.SH,600379.SH,600380.SH,600381.SH,600382.SH,600383.SH,600385.SH,600386.SH,600387.SH,600388.SH,600389.SH,600390.SH,600391.SH,600392.SH,600393.SH,600395.SH,600396.SH,600397.SH,600398.SH,600399.SH,600400.SH,600401.SH,600403.SH,600405.SH,600406.SH,600408.SH,600409.SH,600410.SH,600415.SH,600416.SH,600418.SH,600419.SH,600420.SH,600421.SH,600422.SH,600423.SH,600425.SH,600426.SH,600428.SH,600429.SH,600432.SH,600433.SH,600435.SH,600436.SH,600438.SH,600439.SH,600444.SH,600446.SH,600448.SH,600449.SH,600452.SH,600455.SH,600456.SH,600458.SH,600459.SH,600460.SH,600461.SH,600462.SH,600463.SH,600466.SH,600467.SH,600468.SH,600469.SH,600470.SH,600475.SH,600476.SH,600477.SH,600478.SH,600479.SH,600480.SH,600481.SH,600482.SH,600483.SH,600485.SH,600486.SH,600487.SH,600488.SH,600489.SH,600490.SH,600491.SH,600493.SH,600495.SH,600496.SH,600497.SH,600498.SH,600499.SH,600500.SH,600501.SH,600502.SH,600503.SH,600505.SH,600506.SH,600507.SH,600508.SH,600509.SH,600510.SH,600511.SH,600512.SH,600513.SH,600515.SH,600516.SH,600517.SH,600518.SH,600519.SH,600520.SH,600521.SH,600522.SH,600523.SH,600525.SH,600526.SH,600527.SH,600528.SH,600529.SH,600530.SH,600531.SH,600532.SH,600533.SH,600535.SH,600536.SH,600537.SH,600538.SH,600539.SH,600540.SH,600543.SH,600545.SH,600546.SH,600547.SH,600548.SH,600549.SH,600550.SH,600551.SH,600552.SH,600555.SH,600556.SH,600557.SH,600558.SH,600559.SH,600560.SH,600561.SH,600562.SH,600563.SH,600565.SH,600566.SH,600567.SH,600568.SH,600569.SH,600570.SH,600571.SH,600572.SH,600573.SH,600575.SH,600576.SH,600577.SH,600578.SH,600579.SH,600580.SH,600581.SH,600582.SH,600583.SH,600584.SH,600585.SH,600586.SH,600587.SH,600588.SH,600589.SH,600590.SH,600592.SH,600593.SH,600594.SH,600595.SH,600596.SH,600597.SH,600598.SH,600599.SH,600600.SH,600601.SH,600602.SH,600603.SH,600604.SH,600605.SH,600606.SH,600608.SH,600609.SH,600610.SH,600611.SH,600612.SH,600613.SH,600614.SH,600615.SH,600616.SH,600617.SH,600618.SH,600619.SH,600620.SH,600621.SH,600622.SH,600623.SH,600624.SH,600626.SH,600628.SH,600629.SH,600630.SH,600633.SH,600634.SH,600635.SH,600636.SH,600637.SH,600638.SH,600639.SH,600640.SH,600641.SH,600642.SH,600643.SH,600644.SH,600645.SH,600647.SH,600648.SH,600649.SH,600650.SH,600651.SH,600652.SH,600653.SH,600654.SH,600655.SH,600657.SH,600658.SH,600660.SH,600661.SH,600662.SH,600663.SH,600664.SH,600665.SH,600666.SH,600667.SH,600668.SH,600671.SH,600673.SH,600674.SH,600675.SH,600676.SH,600677.SH,600678.SH,600679.SH,600680.SH,600681.SH,600682.SH,600683.SH,600684.SH,600685.SH,600686.SH,600687.SH,600688.SH,600689.SH,600690.SH,600691.SH,600692.SH,600693.SH,600694.SH,600695.SH,600696.SH,600697.SH,600698.SH,600699.SH,600701.SH,600702.SH,600703.SH,600704.SH,600705.SH,600706.SH,600707.SH,600708.SH,600710.SH,600711.SH,600712.SH,600713.SH,600714.SH,600715.SH,600716.SH,600717.SH,600718.SH,600719.SH,600720.SH,600721.SH,600722.SH,600723.SH,600724.SH,600725.SH,600726.SH,600727.SH,600728.SH,600729.SH,600730.SH,600731.SH,600732.SH,600733.SH,600734.SH,600735.SH,600736.SH,600737.SH,600738.SH,600739.SH,600740.SH,600741.SH,600742.SH,600743.SH,600744.SH,600745.SH,600746.SH,600747.SH,600748.SH,600749.SH,600750.SH,600751.SH,600753.SH,600754.SH,600755.SH,600756.SH,600757.SH,600758.SH,600759.SH,600760.SH,600761.SH,600763.SH,600764.SH,600765.SH,600766.SH,600767.SH,600768.SH,600769.SH,600770.SH,600771.SH,600773.SH,600774.SH,600775.SH,600776.SH,600777.SH,600778.SH,600779.SH,600780.SH,600781.SH,600782.SH,600783.SH,600784.SH,600785.SH,600787.SH,600789.SH,600790.SH,600791.SH,600792.SH,600793.SH,600794.SH,600795.SH,600796.SH,600797.SH,600798.SH,600800.SH,600801.SH,600802.SH,600803.SH,600804.SH,600805.SH,600806.SH,600807.SH,600808.SH,600809.SH,600810.SH,600811.SH,600812.SH,600814.SH,600815.SH,600816.SH,600817.SH,600818.SH,600819.SH,600820.SH,600821.SH,600822.SH,600823.SH,600824.SH,600825.SH,600826.SH,600827.SH,600828.SH,600829.SH,600830.SH,600831.SH,600833.SH,600834.SH,600835.SH,600836.SH,600837.SH,600838.SH,600839.SH,600841.SH,600843.SH,600844.SH,600845.SH,600846.SH,600847.SH,600848.SH,600850.SH,600851.SH,600853.SH,600854.SH,600855.SH,600856.SH,600857.SH,600858.SH,600859.SH,600860.SH,600861.SH,600862.SH,600863.SH,600864.SH,600865.SH,600866.SH,600867.SH,600868.SH,600869.SH,600870.SH,600871.SH,600872.SH,600873.SH,600874.SH,600875.SH,600876.SH,600877.SH,600879.SH,600880.SH,600881.SH,600882.SH,600883.SH,600884.SH,600885.SH,600886.SH,600887.SH,600888.SH,600889.SH,600890.SH,600891.SH,600892.SH,600893.SH,600894.SH,600895.SH,600896.SH,600897.SH,600898.SH,600900.SH,600908.SH,600909.SH,600917.SH,600919.SH,600926.SH,600936.SH,600939.SH,600958.SH,600959.SH,600960.SH,600961.SH,600962.SH,600963.SH,600965.SH,600966.SH,600967.SH,600969.SH,600970.SH,600971.SH,600973.SH,600975.SH,600976.SH,600977.SH,600978.SH,600979.SH,600980.SH,600981.SH,600982.SH,600983.SH,600984.SH,600985.SH,600986.SH,600987.SH,600988.SH,600990.SH,600992.SH,600993.SH,600995.SH,600996.SH,600997.SH,600998.SH,600999.SH,601000.SH,601001.SH,601002.SH,601003.SH,601005.SH,601006.SH,601007.SH,601008.SH,601009.SH,601010.SH,601011.SH,601012.SH,601015.SH,601016.SH,601018.SH,601020.SH,601021.SH,601028.SH,601038.SH,601058.SH,601069.SH,601088.SH,601098.SH,601099.SH,601100.SH,601101.SH,601106.SH,601107.SH,601111.SH,601113.SH,601116.SH,601117.SH,601118.SH,601126.SH,601127.SH,601128.SH,601137.SH,601139.SH,601155.SH,601158.SH,601163.SH,601166.SH,601168.SH,601169.SH,601177.SH,601179.SH,601186.SH,601188.SH,601198.SH,601199.SH,601208.SH,601211.SH,601212.SH,601216.SH,601218.SH,601222.SH,601225.SH,601226.SH,601229.SH,601231.SH,601233.SH,601238.SH,601258.SH,601288.SH,601311.SH,601313.SH,601318.SH,601328.SH,601333.SH,601336.SH,601339.SH,601368.SH,601369.SH,601375.SH,601377.SH,601388.SH,601390.SH,601398.SH,601500.SH,601515.SH,601518.SH,601519.SH,601555.SH,601558.SH,601566.SH,601567.SH,601579.SH,601588.SH,601595.SH,601599.SH,601600.SH,601601.SH,601607.SH,601608.SH,601611.SH,601616.SH,601618.SH,601628.SH,601633.SH,601636.SH,601666.SH,601668.SH,601669.SH,601677.SH,601678.SH,601688.SH,601689.SH,601699.SH,601700.SH,601717.SH,601718.SH,601727.SH,601766.SH,601777.SH,601788.SH,601789.SH,601798.SH,601799.SH,601800.SH,601801.SH,601808.SH,601811.SH,601818.SH,601857.SH,601858.SH,601866.SH,601872.SH,601877.SH,601880.SH,601881.SH,601882.SH,601886.SH,601888.SH,601890.SH,601898.SH,601899.SH,601900.SH,601901.SH,601908.SH,601918.SH,601919.SH,601928.SH,601929.SH,601933.SH,601939.SH,601958.SH,601965.SH,601966.SH,601968.SH,601969.SH,601985.SH,601988.SH,601989.SH,601991.SH,601992.SH,601996.SH,601997.SH,601998.SH,601999.SH,603000.SH,603001.SH,603002.SH,603003.SH,603005.SH,603006.SH,603007.SH,603008.SH,603009.SH,603010.SH,603011.SH,603012.SH,603015.SH,603016.SH,603017.SH,603018.SH,603019.SH,603020.SH,603021.SH,603022.SH,603023.SH,603025.SH,603026.SH,603027.SH,603028.SH,603029.SH,603030.SH,603031.SH,603032.SH,603033.SH,603035.SH,603036.SH,603037.SH,603038.SH,603039.SH,603040.SH,603058.SH,603060.SH,603066.SH,603067.SH,603069.SH,603077.SH,603085.SH,603088.SH,603089.SH,603090.SH,603098.SH,603099.SH,603100.SH,603101.SH,603108.SH,603111.SH,603116.SH,603117.SH,603118.SH,603123.SH,603126.SH,603128.SH,603131.SH,603158.SH,603159.SH,603160.SH,603165.SH,603166.SH,603167.SH,603168.SH,603169.SH,603177.SH,603186.SH,603188.SH,603189.SH,603198.SH,603199.SH,603203.SH,603208.SH,603218.SH,603222.SH,603223.SH,603227.SH,603228.SH,603238.SH,603239.SH,603258.SH,603266.SH,603268.SH,603288.SH,603298.SH,603299.SH,603300.SH,603306.SH,603308.SH,603309.SH,603311.SH,603313.SH,603315.SH,603318.SH,603319.SH,603322.SH,603323.SH,603328.SH,603330.SH,603333.SH,603336.SH,603337.SH,603338.SH,603339.SH,603345.SH,603355.SH,603358.SH,603360.SH,603366.SH,603368.SH,603369.SH,603377.SH,603389.SH,603393.SH,603398.SH,603399.SH,603416.SH,603421.SH,603429.SH,603444.SH,603456.SH,603508.SH,603515.SH,603518.SH,603519.SH,603520.SH,603528.SH,603555.SH,603556.SH,603558.SH,603559.SH,603566.SH,603567.SH,603568.SH,603569.SH,603577.SH,603579.SH,603585.SH,603588.SH,603589.SH,603598.SH,603599.SH,603600.SH,603601.SH,603603.SH,603606.SH,603608.SH,603609.SH,603611.SH,603615.SH,603616.SH,603618.SH,603626.SH,603628.SH,603633.SH,603636.SH,603637.SH,603638.SH,603639.SH,603658.SH,603660.SH,603663.SH,603667.SH,603668.SH,603669.SH,603677.SH,603678.SH,603686.SH,603688.SH,603689.SH,603690.SH,603696.SH,603698.SH,603699.SH,603701.SH,603703.SH,603708.SH,603716.SH,603718.SH,603726.SH,603727.SH,603729.SH,603737.SH,603738.SH,603766.SH,603777.SH,603778.SH,603779.SH,603788.SH,603789.SH,603798.SH,603799.SH,603800.SH,603806.SH,603808.SH,603816.SH,603817.SH,603818.SH,603819.SH,603822.SH,603823.SH,603828.SH,603838.SH,603839.SH,603843.SH,603858.SH,603859.SH,603861.SH,603866.SH,603868.SH,603869.SH,603877.SH,603878.SH,603881.SH,603883.SH,603885.SH,603886.SH,603887.SH,603888.SH,603889.SH,603898.SH,603899.SH,603900.SH,603901.SH,603909.SH,603918.SH,603919.SH,603928.SH,603929.SH,603936.SH,603939.SH,603958.SH,603959.SH,603966.SH,603968.SH,603969.SH,603977.SH,603979.SH,603986.SH,603987.SH,603988.SH,603989.SH,603990.SH,603993.SH,603996.SH,603997.SH,603998.SH,603999.SH","pre_close,close,amt,free_turn",dateString)
            dataPd = pd.DataFrame(data.Data)
            dataPd = dataPd.transpose()
            dataPd = dataPd.dropna()
    
            if dataPd.empty:
                continue
            else:
                mean_vals = dataPd.mean()
                sd_vals = dataPd.std()
                #dataPd.fillna(mean_vals,inplace=True)
                #normalized data
                dataPdNorm = (dataPd - mean_vals)/sd_vals
                
                xTrain = dataPdNorm.iloc[:,[0,2,3]]
                yTrain = dataPdNorm.iloc[:,1]   

                pricePrediction = linear_model.LinearRegression()
                pricePrediction.fit(xTrain,yTrain)
                theta.append(pricePrediction.coef_)
#                print(yTrain)
#                print(pricePrediction.predict(xTrain))
                R.append(self.get_reward(yTrain,pricePrediction.predict(xTrain)))
    
        thetaPd = pd.DataFrame(theta)
        summary = thetaPd.describe()
        #print(R,'\n')
        #print(theta)
        sys.stdout.write("\t""pre_close \t""amt \t""free_turn")
        print(summary)
    
if __name__ == '__main__' :
    #simpleBox(target_url = target_url)
    summary1 = strategeOne(datelist = datelist)
    summary1.summary()