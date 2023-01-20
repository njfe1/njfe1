const h = 150;//初始树干长度
let se = 0;//随机种子
let yoff = 0;//柏林噪声偏移值
function setup() {
    createCanvas(1000, 600);
}

function draw() {
    background(195);
    translate(width / 2, height);//初始树干起点在屏幕底部的中点
    yoff += 0.008//柏林噪声偏移增量
    randomSeed(se);
    branch(h);//开始递归画树枝
}

function branch(h) {
    let sw = map(h, 6, 120, 1, 15);//树枝的粗细根据高度值映射到1-15
    strokeWeight(sw);
    line(0, 0, 0, -h);  //绘制树枝
    translate(0, -h);//坐标原点变换到终点
    h *= random(0.7,0.8);//新的树枝的长度是原来的3/4
    // xoff += 0.1

    if (h > 6) {
        let n = floor(random(1, 4));//随机的树枝数量
        for (let i = 0; i < n; i++) {
            //角度值由柏林噪声生成，如果映射到（-45,45），角度可能会到0，树枝会并拢。如果映射到15~45，会向一边偏斜。
            let theta = map(noise(i, yoff), 0, 1, 15, 37);
            if (i % 2 == 0) theta *= -1;//把上次的角度值取相反数，就不会并拢
            push();//保存当前的坐标状态
            rotate(radians(theta));//旋转一个角度theta
            branch(h);  //递归调用，绘制新的树枝
            pop();//退回到上一个坐标状态
        }

    } else {//在树枝的最终端，绘制树叶
        noStroke();
        fill(0, 255, 0);
        circle(0, 0, 6);
    }
}

function mousePressed() {
    // 点击鼠标，从新的柏林噪声偏移值和新的随机种子开始绘制
    yoff = random(10000);
    se = millis();
} 
