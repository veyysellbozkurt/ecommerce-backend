const mongoose = require('mongoose');

const uri = "mongodb+srv://babamongo:babamongo@cluster0.tlssidq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('MongoDB bağlantısı başarılı!');
  })
  .catch((err) => {
    console.log('MongoDB bağlantı hatası: ', err);
  });