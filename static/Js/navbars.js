const services_dropDown_btn = document.getElementById('services-dropDown-btn'),
    services_dropdown_content = document.getElementById('services-dropdown-content'),
    dropdown_arrow = document.getElementById('dropdown-arrow'),
    tablet_mobile_close_menuBar_btn = document.getElementById('tablet-mobile-close-menuBar-btn'),
    tablet_mobile_open_menuBar_btn = document.getElementById('tablet-mobile-open-menuBar-btn'),
    tablet_mobile_menubar_container = document.getElementById('tablet-mobile-menubar-container'),
    tablet_mobile_menubar_box = document.getElementById('tablet-mobile-menubar-box'),
    tablet_mobile_menubar_ul = document.getElementById('tablet-mobile-menubar-ul'),
    search_container_closeBtn = document.getElementById('search-container-closeBtn'),
    search_box = document.getElementById('search-box'),
    search_container = document.getElementById('search-container'),
    search_openBtn = document.getElementById('search-openBtn'),
    tablet_mobile_search_openBtn = document.getElementById("tablet-mobile-search-openBtn"),
    main_navbar_lang_switcher_btn = document.getElementById('main-navbar-lang-switcher-btn'),
    main_navbar_lang_switcher = document.getElementById('main-navbar-lang-switcher'),
    mobile_navbar_lang_switcher_btn = document.getElementById('mobile-navbar-lang-switcher-btn'),
    mobile_navbar_lang_switcher = document.getElementById('mobile-navbar-lang-switcher');


// to main navbar hidden and appearing
var lastScrollTop = 0;

window.addEventListener("scroll", function () {
    var st = document.documentElement.scrollTop;
    if (st < lastScrollTop) {
        document.getElementById("main-navbar").style.top = "0";
    } else {
        document.getElementById("main-navbar").style.top = "-16vw";
    }
    lastScrollTop = st;
}, false);

var lastScrollTopI = 0;
window.addEventListener('scroll', function () {
    var st = document.documentElement.scrollTop;
    if (st < lastScrollTopI) {
        document.getElementById('responsive-fixed-nav').style.height = '13vw'
    } else {
        document.getElementById('responsive-fixed-nav').style.height = '0'
    }
    lastScrollTopI = st;
}, false)


// for mobile menubar dropdown content toggle things
services_dropDown_btn.addEventListener('click', () => {
    services_dropdown_content.classList.toggle('drop-down-height-toggle')
    dropdown_arrow.classList.toggle('drop-down-arrowDown-transform')
    document.getElementById('fa-paperclip').classList.toggle('this-go-hidden')
})


// for opening and closing mobile menubar
tablet_mobile_open_menuBar_btn.addEventListener('click', () => {
    tablet_mobile_menubar_container.style.visibility = 'visible';
    tablet_mobile_menubar_box.style.width = '70vw';
    setTimeout(() => {
        tablet_mobile_menubar_ul.style.opacity = '100%';
        tablet_mobile_close_menuBar_btn.style.opacity = '100%'
    }, 500)
})

tablet_mobile_close_menuBar_btn.addEventListener('click', () => {
    tablet_mobile_menubar_ul.style.opacity = '0';
    tablet_mobile_close_menuBar_btn.style.opacity = '0'
    setTimeout(() => {
        tablet_mobile_menubar_container.style.visibility = 'hidden';
        tablet_mobile_menubar_box.style.width = '0';
    }, 1000)
})

tablet_mobile_menubar_container.addEventListener('click', (target) => {
    if (target.target === tablet_mobile_menubar_container ) {
        tablet_mobile_menubar_ul.style.opacity = '0';
        tablet_mobile_close_menuBar_btn.style.opacity = '0'
        setTimeout(() => {
            tablet_mobile_menubar_container.style.visibility = 'hidden';
            tablet_mobile_menubar_box.style.width = '0';
        }, 1000)
    }
})


// for opening and closing search container
search_openBtn.addEventListener("click", () => {
    search_container.style.display = 'flex'
    setTimeout(() => {
        search_box.style.width = '50vw'
    }, 300)
})

search_container_closeBtn.addEventListener('click', () => {
    search_box.style.width = '0'
    setTimeout(() => {
        search_container.style.display = 'none'
    }, 1000)
})
// for mobile and tablet
tablet_mobile_search_openBtn.addEventListener('click', () => {
    search_container.style.display = 'flex'
    setTimeout(() => {
        search_box.style.width = '70vw'
    }, 300)
})



// to submit and switch the language when language options change
main_navbar_lang_switcher.addEventListener('change', () => {
    main_navbar_lang_switcher_btn.form.submit()
})
mobile_navbar_lang_switcher.addEventListener('change', () => {
    mobile_navbar_lang_switcher_btn.form.submit()
})
