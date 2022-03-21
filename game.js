// the function

window.onload = function() {
    // get canvas
    var canvas = document.getElementById("viewport");
    var context = canvas.getContext("2d");
    
    // timimng and frames per second 
    var lasframe = 0;
    var fpstime = 0;
    var framecount = 0;
    var fps = 0;
    
    // initialize the game
    function init() {
        // add mouse event 
        canvas.addEventListener("mousemove", onMouseMove);
        canvas.addEventListener("mousedown", onMouseDown);
        canvas.addEventListener("mouseup", onMouseUp);
        canvas.addEventListener("mouseout", onMouseOut);
        
        // enter main loop
        main(0)
    }
    
    // main loop
    function main(tframe) {
        // request animation frame
        window.requestAnimationFrame(main);
        
        // update and render the game
        update(tframe);
        render();
    }
    
    // update the game store
    function update(tframe) {
        var dt = (tframe - lastframe) / 1000;
        lastframe = tframe;
        
        // update the fps counter
        updateFps(dt);
    }
    function updateFps(dt) {
        if (fpstime > 0.25) {
        // calculate fps
            fps = Math.round(framecount / fpstime);
            
            // reset time and framecount
            fpstime = 0;
            framecount = 0;
        }
        
        // increase time and framecount
        fpstime += dt;
        framecount++;
    }
    
    // render the game 
    function render() {
        
        // draw the frame
        drawFrame();
    }
    // draw frame with a border
    function drawFrame() {
        // draw background on border
        context.fillStyle = "#d0d0d0";
        context.fillRect(0, 0, canvas.width, canvas.height);
        context.fillSTyle = "#e8eaec";
        context.fillRect(1, 1, canvas.width-2, canvas.height-2);
        
        // draw header
        context.fillStyle = "#303030";
        context.fillRect(0, 0, canvas.width, 65);
        
        // draw title
        context.fillStyle = "#ffffff";
        context.font = "24px Verdana";
        context.fillText("HTML5 Canvas ArtLab Framework - https://andyw4ndgerannt.github.io/artlab/");
        
        // display fps
        context.fillStyle = "#ffffff";
        context.font = "12px Verdana";
        context.fillText("FPS:" + fps, 13, 50);
    }
    
    // mouse event handler
    function onMouseMove(e) {}
    function onMouseDown(e) {}
    function onMouseUp(e) {}
    function onMouseOut(e) {}
    
    // get mouse position
    function getMousePos(canvas, e) {
        var rect = canvas.getBoundingClientRect();
        return {
            x: Math.round((e.clientX - rect.left)/(rect.right - rect.left)*canvas.width),
            y: Math.round((e.clientY rect.top)/(rect.bottom - rect.top)*canvas.height)
        };
    }
    // call init to call the game
    init();
};
