import puppeteer from 'puppeteer';
import fs from 'node:fs';
import axios from 'axios';

// Define URLs
const root = 'https://www.berlinpackaging.eu';
const glassJars = '/en/51/glass-food-packaging';
const plasticJars = '/en/112/plastic-jars';
const glassBottles = '/en/211/empty-glass-bottles';
const plasticBottles = '/en/94/plastic-bottles';

// Launch the browser and open a new blank page
const browser = await puppeteer.launch();
var page = await browser.newPage();

// Navigate the page to a URL
await page.goto(root + plasticBottles);

// Set screen size
await page.setViewport({ width: 1080, height: 1024 });

// Define container variables
let elementHandle;
let closureElements;

// Fetch URLs of all jars in webpage
try {
    elementHandle = await page.$('#listaProductos');
    if (elementHandle === null) {
        throw new Error('Element with specified ID not found.');
    }
    // Further operations with elementHandle
    closureElements = await page.evaluate(el => Array.from(
        el.querySelectorAll('a[href]'),
        a => a.getAttribute('href')
    ), elementHandle);
    console.log(closureElements.length)
} catch (error) {
    console.error('Error during element retrieval:', error.message);
}

// Define downloading function
async function downloadImage(url, filename) {
    const response = await axios.get(url, { responseType: 'arraybuffer' });

    fs.writeFile(filename, response.data, (err) => {
        if (err) throw err;
        console.log('Image downloaded successfully!');
    });
}

// Process URLs and download images
if (closureElements.length > 0) {
    for (let i = 0; i < closureElements.length; i++) {
        try {
            console.log(i + 1);
            await page.goto(root + closureElements[i]);
            let imageHandle = await page.$('div.swiper-wrapper');
            if (imageHandle === null) {
                throw new Error('Element with specified class not found.');
            }
            let imageElements = await page.evaluate(el => Array.from(
                el.querySelectorAll('img'),
                a => a.src
            ), imageHandle);
            for(let j = 0; j < imageElements.length; j++){
                await downloadImage(imageElements[j], 'plasticBottles/' + i.toString() + '.jpg');
            }
            console.log(imageElements);
        } catch (error) {
            console.log(error);
            continue
        }
    }
}

console.log(closureElements);

// Close webpage reference
await browser.close();