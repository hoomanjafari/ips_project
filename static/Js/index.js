// to title border and title mini border apear on scrolling in any different screen width


const project_title_border = document.getElementById('project-title-border'),
    project_title_mini_border = document.getElementById('project-title-mini-border'),
    ips_spaces_title_border = document.getElementById("ips-spaces-title-border"),
    ips_spaces_title_mini_border = document.getElementById('ips-spaces-title-mini-border');

window.addEventListener('scroll', () => {
    if (screen.width >= 769) {
        setTimeout(() => {
            if (window.scrollY >= 200) {
                ips_spaces_title_border.style.width = '26vw'
                ips_spaces_title_mini_border.style.width = '13vw'
            }

            else {
                ips_spaces_title_border.style.width = '0'
                ips_spaces_title_mini_border.style.width = '0'
            }
        }, 500)
    }
    else if (screen.width <= 768 && screen.width >= 426) {
        setTimeout(() => {
            if (window.scrollY >= 100) {
                ips_spaces_title_border.style.width = '35vw'
                ips_spaces_title_mini_border.style.width = '21vw'
            }

            else {
                ips_spaces_title_border.style.width = '0'
                ips_spaces_title_mini_border.style.width = '0'
            }
        }, 500)
    }
})




window.addEventListener('scroll', () => {
    console.log(window.scrollY)
    if (screen.width >= 769) {
        setTimeout(() => {
            if (window.scrollY >= 1600) {
                project_title_border.style.width = '26vw'
                project_title_mini_border.style.width = '13vw'
            }
            else {
                project_title_border.style.width = '0'
                project_title_mini_border.style.width = '0'
            }
        }, 500)
    }
    else if (screen.width <= 768 && screen.width >= 426) {
        setTimeout(() => {
            if (window.scrollY >= 1200) {
                project_title_border.style.width = '35vw'
                project_title_mini_border.style.width = '21vw'
            }
            else {
                project_title_border.style.width = '0'
                project_title_mini_border.style.width = '0'
            }
        }, 500)
    }
    else if (screen.width <= 425) {
        setTimeout(() => {
            if (window.scrollY >= 2300) {
                project_title_border.style.width = '52vw'
                project_title_mini_border.style.width = '31vw'
            }
            else {
                project_title_border.style.width = '0'
                project_title_mini_border.style.width = '0'
            }
        }, 500)
    }
})
