// to animate project boxes on scrolling
var ips_project_box = document.querySelectorAll('.ips-project-box');
ips_project_box.forEach(box => {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: box,
            start: 'top 90%',
            end: 'bottom center',
            scrub: false,
            markers: false,
            // toggleActions: 'play none none reverse'
        }
    })
    tl.to(box , {
        opacity: 100,
        duration: 1,
    })
})









// get CSRF_TOKEN from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');










// filtering buttons
const project_filtering = document.querySelectorAll('#project-filtering');
const ips_projects_container = document.getElementById('ips-projects-container');
const project_filtering_label = document.querySelectorAll('.project-filtering-label');

// to give 100 opacity to all the boxes on scroll trigger
function test(){
    ips_project_box.forEach(box => {
        let tl = gsap.timeline({
            scrollTrigger: {
                trigger: box,
                start: 'top 90%',
                end: 'bottom center',
                scrub: false,
                markers: false,
                // toggleActions: 'play none none reverse'
            }
        })
        tl.to(box , {
            opacity: 100,
            duration: 1,
        })
    })
}

// to show the template of the selected filter
function filteringChangeTemplate() {
    fetch('/ips-projects/filtering_template_change/', {
        method: 'GET',
    })
    .then(res => res.text())
    .then(html => {
        ips_projects_container.innerHTML = ''
        ips_projects_container.innerHTML = html
        ips_project_box = document.querySelectorAll('.ips-project-box');
        test()
    })
}

// to take the selected filter id_number and send it to server for query
function projectFiltering(id) {
    fetch('/ips-projects/projects_filtering/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'selected_filter_value': id
        })
    })
    .then(res => res.json())
    .then(data => {
        filteringChangeTemplate()
    })
}


// to clearing the active selected filtering by clearing it border
function clearActiveFilters() {
    project_filtering_label.forEach(item => {
        item.classList.remove('selected-filter-active')
    })
}


// to active the selected filtering by give it a border
project_filtering_label.forEach(item => {
    item.addEventListener('click', () => {
        clearActiveFilters()
        item.classList.add('selected-filter-active')
    })
})


// to take the selected filter field id_number and give it to the projectFiltering() function to send it to server
project_filtering.forEach(item => {
    let project_id = null
    item.addEventListener('click', () =>{
        project_id = item.value
        projectFiltering(project_id)
    })
})


// with this function on the template that is created for filtered projects user can change the pages if there are more pages for that specific project
function goToPage(page_number) {
    console.log('mona monaa is', page_number)
    fetch(`/ips-projects/filtering_template_change/?page=${page_number}`, {
        method: 'GET',
    })
    .then(res => res.text())
    .then(html => {
        ips_projects_container.innerHTML = ''
        ips_projects_container.innerHTML = html
        ips_project_box = document.querySelectorAll('.ips-project-box');
        test()
    })
}
