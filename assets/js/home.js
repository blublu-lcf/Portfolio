// 获取所有的导航项
const navItems = document.querySelectorAll('.nav-item');

const thisitem = document.getElementById("Home");
thisitem.classList.toggle('active')

// 遍历所有导航项，并添加点击事件监听
navItems.forEach(item => {
    item.addEventListener('click', function() {
        // 移除其他nav-item的active类
        navItems.forEach(nav => nav.classList.remove('active'));

        // 给当前点击的nav-item添加active类
        this.classList.add('active');
    });
});

const element = document.getElementById('overlay7');
const rect = element.getBoundingClientRect();
const elementTop = rect.top; // 获取元素顶部距离视口的距离
console.log(elementTop); // 打印出元素的顶部位置

const overlayText = document.getElementById('overlay');
const threshold = 700;
overlayText.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold) {
        overlayText.style.opacity = 1;
    }
});
const overlayText1 = document.getElementById('overlay1');
const threshold1 = 1300;
overlayText1.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold1) {
        overlayText1.style.opacity = 1;
    }
});
const overlayText2 = document.getElementById('overlay2');
const threshold2 = 1770;
overlayText2.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold2) {
        overlayText2.style.opacity = 1;
    }
});
const overlayText3 = document.getElementById('overlay3');
const threshold3 = 2800;
overlayText3.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold3) {
        overlayText3.style.opacity = 1;
    }
});
const overlayText4 = document.getElementById('overlay4');
const threshold4 = 3600;
overlayText4.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold4) {
        overlayText4.style.opacity = 1;
    }
});
const overlayText5 = document.getElementById('overlay5');
const threshold5 = 3900;
overlayText5.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold5) {
        overlayText5.style.opacity = 1;
    }
});
const overlayText6 = document.getElementById('overlay6');
const threshold6 = 4200;
overlayText6.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold6) {
        overlayText6.style.opacity = 1;
    }
});
const overlayText7 = document.getElementById('overlay7');
const threshold7 = 4600;
overlayText7.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold7) {
        overlayText7.style.opacity = 1;
    }
});
const overlayText8 = document.getElementById('overlay8');
const threshold8 = 5500;
overlayText8.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold8) {
        overlayText8.style.opacity = 1;
    }
});
const overlayText9 = document.getElementById('overlay9');
const threshold9 = 5700;
overlayText9.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold9) {
        overlayText9.style.opacity = 1;
    }
});
const overlayText10 = document.getElementById('overlay10');
const threshold10 = 6100;
overlayText10.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold10) {
        overlayText10.style.opacity = 1;
    }
});
const overlayText11 = document.getElementById('overlay11');
const threshold11 = 7000;
overlayText11.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold11) {
        overlayText11.style.opacity = 1;
    }
});
const overlayText12 = document.getElementById('overlay12');
const threshold12 = 7900;
overlayText12.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold12) {
        overlayText12.style.opacity = 1;
    }
});
const overlayText13 = document.getElementById('overlay13');
const threshold13 = 8300;
overlayText13.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold13) {
        overlayText13.style.opacity = 1;
    }
});
const overlayText14 = document.getElementById('overlay14');
const threshold14 = 8500;
overlayText14.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold14) {
        overlayText14.style.opacity = 1;
    }
});
const overlayText15 = document.getElementById('overlay15');
const threshold15 = 8900;
overlayText15.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold15) {
        overlayText15.style.opacity = 1;
    }
});
const overlayText16 = document.getElementById('overlay16');
const threshold16 = 9200;
overlayText16.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold16) {
        overlayText16.style.opacity = 1;
    }
});
const overlayText17 = document.getElementById('overlay17');
const threshold17 = 9500;
overlayText17.style.opacity = 0;
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > threshold17) {
        overlayText17.style.opacity = 1;
    }
});
