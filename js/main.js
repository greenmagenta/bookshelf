/* init */
hljs.initHighlightingOnLoad();
mermaid.initialize({
	startOnLoad:true,
	securityLevel:'loose'
});

/* sidebar */
var state = true;
if($(window).width() < 600){
	state = !state;
}

$(function(){
	$("#toggle-sidebar").click(function(){
	if(state){
		$("div.sidebar").css("left", "-220px");
		$("div.top").css("left", "-220px");
		$("div.content").css("left", "0");
		$("div.content").css("right", "0");
		$("div.side-action").css("width", "0");
	}
	else{
		$("div.sidebar").css("left", "0");
		$("div.top").css("left", "0");
		$("div.side-action").css("width", "203px");
		if($(window).width() < 600){
			$("div.content").css("left", "220px");
			$("div.content").css("right", "-220px");
		}
		else{
			$("div.content").css("left", "220px");
		}
	}
	state = !state;
	});
});

/* nav buttons */
function index_pages() {
	var page_list = [];
	var pages = document.querySelectorAll('div.sidebar a');
	for(var i = 0; i< pages.length; i++){
		page_list.push(pages[i].getAttribute("href"));
	}
	return page_list;
}

function move_to(dir) {
	var page_list = index_pages();
	var path = window.location.pathname;
	var page = path.split("/").pop();
	var position = page_list.indexOf(page);

	if(dir == 0){
		if(position == 0){
			window.location.href = page_list[page_list.length-1];
		}
		else{
			window.location.href = page_list[position-1];
		}
	}
	else if (dir == 1){
		if(position == page_list.length-1){
			window.location.href = page_list[0];
		}
		else{
			window.location.href = page_list[position+1];
		}
	}
}