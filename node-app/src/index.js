require('dotenv').config();
const express = require('express');

const app = express();
const port = process.env.PORT || 3000;
const envMessage = process.env.APP_MESSAGE || "Default Node.js Config";

app.get('/', (req, res) => {
    res.json({ 
        status: "active", 
        message: envMessage, 
        framework: "Node.js" 
    });
});

app.listen(port, () => {
    console.log(`Service initialized on port ${port}`);
});
