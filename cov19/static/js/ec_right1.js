var ec_right1 = echarts.init(document.getElementById('r1'));
var ec_right1_option = {
	//标题样式
	title : {
	    text : "湖北以外确诊TOP10",
	    textStyle : {
	        color : 'black',
	    },
	    left : 'left'
	},
	  color: ['#db1e24'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%"
    }]
};
ec_right1.setOption(ec_right1_option)