import puppeteer from 'puppeteer';
import fs from 'node:fs';

// Define page urls
const root = 'https://www.berlinpackaging.eu';
const glassJars = root + '/en/52/glass-jars-for-food';
const plasticJars = root + '/en/112/plastic-jars';
const hermeticJars = root + '/en/54/le-parfait-airtight-hermetic-jars';
const squareJars = root + '/en/323/square-glass-jars';
const candyJars = root + '/en/230/candy-glass-jars';
const weckJars = root + '/en/335/jars-weck';
const foodJars = root + '/en/51/glass-food-packaging';

// Launch the browser and open a new blank page
const browser = await puppeteer.launch();
var page = await browser.newPage();

// Navigate the page to a URL
await page.goto(foodJars);

// Set screen size
await page.setViewport({ width: 1080, height: 1024 });

let elementHandle;
let jarElements;
// Fetch URLs of all jars in webpage
try {
    elementHandle = await page.$('#listaProductos');
    if (elementHandle === null) {
        throw new Error('Element with specified ID not found.');
    }
    // Further operations with elementHandle
    jarElements = await page.evaluate(el => Array.from(
        el.querySelectorAll('a[href]'),
        a => a.getAttribute('href')
    ), elementHandle);
    console.log(jarElements.length)
} catch (error) {
    console.error('Error during element retrieval:', error.message);
}
// Process jar URLs and get attributes
if (jarElements.length > 0) {
    for (let i = 0; i < jarElements.length; i++) {
        try {
            console.log(i + 1);
            await page.goto(root + jarElements[i]);
            let tableHandle = await page.$('table.w-full.mb-8');
            if (tableHandle === null) {
                throw new Error('Element with specified class not found.');
            }
            let tableElements = await page.evaluate(el => Array.from(
                el.querySelectorAll('td'),
                a => a.innerText
            ), tableHandle);
            fs.appendFile('data/food_jars.txt', JSON.stringify( tableElements ) + '\n', (err) => {
                if (err) throw err;
            });
        } catch (error) {
            console.log(error);
            continue
        }
    }
}

await browser.close();