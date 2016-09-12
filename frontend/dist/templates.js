angular.module('RPiCar').run(['$templateCache', function($templateCache) {
    $templateCache.put('controllers/car.html',
        "<style type=\"text/css\">\n    body {\n        background: ${BGCOLOR};\n        text-align: center;\n    }\n    #videoCanvas {\n        /* Always stretch the canvas to 640x480, regardless of its\n        internal size. */\n        width: ${WIDTH}px;\n        height: ${HEIGHT}px;\n    }\n</style>\n\n<h1>\n    {{ car.name }}\n    <small>{{ car.address }}</small>\n</h1>\n\n\n<canvas id=\"videoCanvas\" width=\"${WIDTH}\" height=\"${HEIGHT}\">\n    <p>\n        Please use a browser that supports the Canvas Element, like\n        <a href=\"http://www.google.com/chrome\">Chrome</a>,\n        <a href=\"http://www.mozilla.com/firefox/\">Firefox</a>,\n        <a href=\"http://www.apple.com/safari/\">Safari</a> or Internet Explorer 10\n    </p>\n</canvas>\n<script type=\"text/javascript\">\n    // Show loading notice\n    var canvas = document.getElementById('videoCanvas');\n    var ctx = canvas.getContext('2d');\n    ctx.fillStyle = '${COLOR}';\n    ctx.fillText('Loading...', canvas.width/2-30, canvas.height/3);\n\n    // Setup the WebSocket connection and start the player\n    var client = new WebSocket('ws://10.0.1.4:8084/');\n    var player = new jsmpeg(client, {canvas:canvas});\n</script>\n\n\n<div ng-keydown=\"keyDownHandler($event)\" ng-keyup=\"keyUpHandler($event)\">\n\n    <div class=\"row\">\n        <div class=\"col-md-offset-2 col-md-8\">\n            <button id=\"forwardBtn\" type=\"button\" class=\"btn btn-lg btn-default btn-block\" autofocus\n                    ng-class=\"{'btn-primary': moveStatus.forward}\"\n                    ng-mousedown=\"move('forward', true)\"\n                    ng-mouseup=\"move('forward', false)\"\n                >Forward\n            </button>\n        </div>\n    </div>\n\n\n    <br>\n    <div class=\"row\">\n        <div class=\"col-md-4\">\n            <button id=\"leftBtn\" type=\"button\" class=\"btn btn-lg btn-default btn-block\"\n                    ng-class=\"{'btn-primary': moveStatus.left}\"\n                    ng-mousedown=\"move('left', true)\"\n                    ng-mouseup=\"move('left', false)\"\n                >Left\n            </button>\n        </div>\n\n        <div class=\"col-md-offset-4 col-md-4\">\n            <button id=\"rightBtn\" type=\"button\" class=\"btn btn-lg btn-default btn-block\"\n                    ng-class=\"{'btn-primary': moveStatus.right}\"\n                    ng-mousedown=\"move('right', true)\"\n                    ng-mouseup=\"move('right', false)\"\n                >Right\n            </button>\n        </div>\n    </div>\n\n\n    <br>\n    <div class=\"row\">\n        <div class=\"col-md-offset-2 col-md-8\">\n            <button id=\"reverseBtn\" type=\"button\" class=\"btn btn-lg btn-default btn-block\"\n                    ng-class=\"{'btn-primary': moveStatus.reverse}\"\n                    ng-mousedown=\"move('reverse', true)\"\n                    ng-mouseup=\"move('reverse', false)\"\n                >Reverse\n            </button>\n        </div>\n    </div>\n</div>\n\n\n<br>\n<ul class=\"list-group\">\n    <li class=\"list-group-item\" ng-repeat=\"item in commandLog\">\n        <span class=\"badge\">{{ item.dt }}</span>\n        {{ item.response }}\n    </li>\n</ul>\n");
}]);
angular.module('RPiCar').run(['$templateCache', function($templateCache) {
    $templateCache.put('controllers/main.html',
        "<h1>Cars</h1>\n\n<div class=\"list-group\">\n    <a href=\"/car/{{ car.id }}\" class=\"list-group-item\" ng-repeat=\"car in cars\">\n        {{ car.name }}\n    </a>\n</div>");
}]);