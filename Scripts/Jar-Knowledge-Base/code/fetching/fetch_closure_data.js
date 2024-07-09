import puppeteer from 'puppeteer';
import fs from 'node:fs';
import { table } from 'node:console';

// Define page urls
const root = 'https://www.berlinpackaging.eu';
const weckClosure = '/en/338/tapas-accesorios-weck'
const twistClosure = '/en/101/twist-off-lids-for-jars';
const fabricCover = '/en/367/fabric-paper-jar-covers';
const parfaitClosure = '/en/217/lids-accessories-le-parfait';
const corkCaps = '/en/102/closure-systems-corks-and-caps';
const corkStoppers = '/en/183/cork-stoppers';
const labClosures = '/en/184/pipettes-stoppers-laboratory';
const crownCaps = '/en/189/crown-caps-bottles';

/**
 * TO DO: for bottles, filter url using the type to determine the type of finish or affordance
 * - Cork: 1
 * - Crown: 6
 * - Press: 3
 * - Screw: 4
 * - Special: 7
 * - Swing Top: 5
 * - Twist-off: 8
 */

// Launch the browser and open a new blank page
const browser = await puppeteer.launch();
var page = await browser.newPage();

// Navigate the page to a URL
await page.goto(root + crownCaps);

// Set screen size
await page.setViewport({ width: 1080, height: 1024 });

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
// Process jar URLs and get attributes
if (closureElements.length > 0) {
    for (let i = 0; i < closureElements.length; i++) {
        try {
            console.log(i + 1);
            await page.goto(root + closureElements[i]);
            let tableHandle = await page.$('table.w-full.mb-8');
            if (tableHandle === null) {
                throw new Error('Element with specified class not found.');
            }
            let tableElements = await page.evaluate(el => Array.from(
                el.querySelectorAll('td'),
                a => a.innerText
            ), tableHandle);
            tableElements.push("Name");
            tableElements.push(closureElements[i].split('/').pop());
            fs.appendFile('data/text/closures/crown_caps.txt', JSON.stringify( tableElements ) + '\n', (err) => {
                if (err) throw err;
            });
        } catch (error) {
            console.log(error);
            continue
        }
    }
}

await browser.close();