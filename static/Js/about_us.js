const onscrolling = document.querySelectorAll('#about-us-on-scroll-event')
const ips_about_us_border = document.querySelectorAll('#ips-about-us-border')
onscrolling.forEach(box => {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: box,
            start: 'top 60%',
            end: 'bottom center',
            scrub: false,
            markers: false
        }
    })

    tl.to(box, {
        opacity: 100,
    })
})

ips_about_us_border.forEach(border => {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: border,
            start: 'top 60%',
            end: 'top 60%',
            scrub: false,
            markers: false
        }
    })
    tl.to(border, {
        borderTop: '4px solid orange'
    })
})
