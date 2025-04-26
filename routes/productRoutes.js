const express = require('express');
const Product = require('../models/Product');
const router = express.Router();

// GET: Ürünleri listele
router.get('/', async (req, res) => {
  try {
    const products = await Product.find();
    res.status(200).json(products);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// POST: Yeni ürün ekle
router.post('/', async (req, res) => {
  const product = new Product({
    name: req.body.name,
    description: req.body.description,
    price: req.body.price,
    stock: req.body.stock,
  });

  try {
    const newProduct = await product.save();
    res.status(201).json(newProduct);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// GET: Belirli bir ürünü getir
router.get('/:id', async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) {
      return res.status(404).json({ message: 'Ürün bulunamadı' });
    }
    res.json(product);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// PUT: Ürünü güncelle
router.put('/:id', async (req, res) => {
  try {
    const updatedProduct = await Product.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true } 
    );
    if (!updatedProduct) {
      return res.status(404).json({ message: 'Ürün bulunamadı' });
    }
    res.json(updatedProduct);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// DELETE: Ürünü sil
router.delete('/:id', async (req, res) => {
  try {
    const deletedProduct = await Product.findByIdAndDelete(req.params.id);
    if (!deletedProduct) {
      return res.status(404).json({ message: 'Ürün bulunamadı' });
    }
    res.json({ message: 'Ürün başarıyla silindi' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
