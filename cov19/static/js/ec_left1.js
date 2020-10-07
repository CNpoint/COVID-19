var ec_left1 = echarts.init(document.getElementById('l1'), "vintage");

var ec_left1_Option = {
	//标题样式
	title: {
		text: "累计趋势",
		textStyle: {
			 color:'black',
		},
		left: 'left',
	},
	tooltip: {
		trigger: 'axis',
		//指示器
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#c64342'
			}
		},
	},
	legend: {
		data: ['累计确诊', '现有疑似', "累计治愈", "累计死亡"],
		left: "right"
	},

	//图形位置
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		//x轴坐标点开始与结束点位置都不在最边缘
		// boundaryGap : true,
		data: []//['03.20', '03.21', '03.22']
	}],
	yAxis: [{
		type: 'value',
		//y轴字体设置
		axisLabel: {
			show: true,
			color: '#040b63',
			fontSize: 12,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//y轴线设置显示
		axisLine: {
			show: true
		},
		//与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#040b63',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [{
		name: "累计确诊",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "现有疑似",
		type: 'line',
		smooth: true,
		data: []
	},
		{
		name: "累计治愈",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "累计死亡",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_left1.setOption(ec_left1_Option)
