


// to title border and title mini border apear on scrolling in any different screen width
const title_border = document.querySelectorAll('.title-border'),
    title_mini_border = document.querySelectorAll('.title-mini-border');



title_border.forEach(title => {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: title,
            start: 'top center',
            end: 'bottom center',
            scrub: true,
            markers: false
        }
    })
    if (screen.width >= 769) {
        tl.to(title, {
            width: '26vw',
        })
    }
    else if (screen.width <= 768 && screen.width >= 426) {
        tl.to(title, {
            width: '50vw',
        })
    }
    else if (screen.width <= 425) {
        tl.to(title, {
            width: '52vw',
        })
    }
})

title_mini_border.forEach(mini_title => {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: mini_title,
            start: 'top center',
            end: 'bottom center',
            scrub: true,
            markers: false
        }
    })
    if (screen.width >= 769) {
        tl.to(mini_title, {
            width: '13vw',
        })
    }
    else if (screen.width <= 768 && screen.width >= 426) {
        tl.to(mini_title, {
            width: '21vw',
        })
    }
    else if (screen.width <= 425) {
        tl.to(mini_title, {
            width: '31vw',
        })
    }
})



const elements = document.querySelectorAll('#opacity100-onload');
elements.forEach(element => {
    let tl = gsap.timeline({
        scrollTrigger: element,
        start: 'center',
        end: 'bottom center',
        scrub: false,
        markers: false
    })
    tl.to(element,{
        opacity: 100,
    })
})


window.addEventListener('load', () => {
    document.getElementById('index-header').style.opacity = '100%'
})