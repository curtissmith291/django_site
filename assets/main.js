
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value



const sendSearchData = (beer) => {
    $.ajax({
        type: 'POST', 
        url: 'beer_rec/search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'beer': beer
        },
        success: (res)=> {
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)) {
                resultsBox.innerHTML = ""
                data.forEach(beer => {
                    resultsBox.innerHTML += `
                    <a href="${url}${beer.pk}" class="item">
                        <div class="row mt-2 mb-2"
                            <div class="col-6"></div>
                                <h6>${beer.beer_name}</h6>
                                <p class="text-muted">${beer.brewery}</p>
                            </div>
                        </div>
                    </a>
                    `
                })
            } else {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>${data}</b>`
                } else {
                    resultsBox.classList.add('not-visible')
                }
            }
        },
        error: (err) => {
            console.log(err)
        }
    })
}


searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if (resultsBox.classList.contains('not-visible')){
        resultsBox.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
})
