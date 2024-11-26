const express = require('express');
const path = require('path');

const app = express();

// Serve the static files from the "frontend" folder
app.use(express.static(path.join(__dirname, '')));

// Route to serve the index.html page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Frontend server is running on http://localhost:${PORT}`);
});