'use strict';

const axios = require('axios');

axios.get('http://127.0.0.1:8001/api/school/lessons')
    .then((response) => {
        console.log(response.data.results);
    })
    .catch((error) => {
        console.log(error);
    })

fetch('http://127.0.0.1:8001/api/school/courses')
    .then(response => console.log(response.json()))
    .catch(error => console.log(error));
