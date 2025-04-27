const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const cors = require('cors');
const productRoutes = require('./routes/productRoutes'); // Ürün routes'ını dahil ettik

dotenv.config();

const app = express();

app.use(cors({
    origin: 'https://babaamet-front.lm.r.appspot.com', // Burada frontend URL'yi belirtiyoruz
    methods: ['GET', 'POST', 'DELETE', 'PUT'], // Hangi metodlara izin verileceğini belirtiyoruz
    allowedHeaders: ['Content-Type'], // Hangi header'lara izin verileceğini belirtiyoruz
  }));
app.use(express.json());

// Ürün API routes'ını kullan
app.use('/products', productRoutes);

mongoose
  .connect(process.env.MONGO_URI)
  .then(() => {
    console.log('MongoDB connection was successful!');
    app.listen(8080, '0.0.0.0', () => {
      console.log('Server running on port 4000 and 0.0.0.0.');
    });
  })
  .catch((err) => {
    console.error('MongoDB connection error:', err.message);
    process.exit(1);
  });