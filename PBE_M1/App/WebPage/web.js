const express = require('express');
const bodyParser = require('body-parser');
const fs=require('fs');
const app = express();
const port = 3000;


//app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

app.set('view engine','ejs');
// Serve the HTML form



app.get('/', (req, res) => {
  res.render('pages/index');
});



app.get('/form', (req, res) => {
  res.render('pages/form');
});



// s'occupe du formulaire pour la configuration du robot
app.post('/form', (req, res) => {
  const data = req.body;
  
  // Conversion des données json en chaine de caractere
  const jsonData = JSON.stringify(data);
  console.log(jsonData); // Pour debug
  
  
  
   fs.writeFileSync('../config.json',jsonData);
  res.render("pages/index");
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
