var ec_right2 = echarts.init(document.getElementById('r2'), "vintage");


var ec_right2_option = {

						title : {
						    text : "复工复课热搜词云图",
						    textStyle : {
						        color : 'black',
						    },
						    left : 'left'
						},
                        tooltip: {
                            show: false
                        },
                        series: [{
                                type: 'wordCloud',

                                gridSize: 1,
                                sizeRange: [12, 55],
                                rotationRange: [-45, 0, 45, 90],

                                textStyle: {
                                    normal: {
                                        color: function () {
                                            return 'rgb(' +
                                                    Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) + ')'
                                        }
                                    }
                                },
                                              // 定义随机颜色
                                right: null,
                                bottom: null,
                                data:  []
                            }]
                    }

ec_right2.setOption(ec_right2_option);
