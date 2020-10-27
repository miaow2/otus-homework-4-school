'use strict';

const axios = require('axios');

axios.get('/api/school/lessons')
    .then((response) => {
        console.log(response.data.results);
    })
    .catch((error) => {
        console.log(error);
    })

fetch('/api/school/courses')
    .then(response => console.log(response.json()))
    .catch(error => console.log(error));
