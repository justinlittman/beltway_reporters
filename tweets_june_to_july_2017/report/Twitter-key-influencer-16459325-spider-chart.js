Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['twitter-numberOfFollowers','twitter-wantsToBeInfluencer','twitter-actualInfluencer','twitter-trustedSource','twitter-mostMentioned','twitter-potentialReach','twitter-potentialConnectors','inDegreeCentrality','twitter-averageMentionsPerTweet',],
datasets : [
{
label: 'ryanbeckwith',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
fill:true,
data : [0.00962075,0.964912,0.00730998,0.212766,0.26477,0.255693,0.217736,0.513848,0.0864802,]
},
{
label: 'Tweeter Average',
backgroundColor: 'rgba(0,255,0,0.2)',
borderColor: 'rgba(0,255,0,1)',
borderWidth: 1,
fill:true,
data : [0.00748346,0.0562464,0.00476542,0.0426335,0.0503075,0.098655,0.0348663,0.0352339,0.090939,]
},
]
}
var context = document.getElementById('Twitter-key-influencer-16459325-spider-chart').getContext("2d");
var chart = new Chart(context, {
		type: 'radar',
		data: data,
		options: {
				autowidth:false,
			scale: { ticks: { min:0, max:1, display:false}}
		}
});

