#!/usr/bin/node
const fs = require('fs');

function concatFiles(sourceFile1, sourceFile2, destinationFile) {
  // Read the content of source file 1
  fs.readFile(sourceFile1, 'utf8', (err, data1) => {
    if (err) {
      console.error(`Error reading source file 1: ${err}`);
      return;
    }

    // Read the content of source file 2
    fs.readFile(sourceFile2, 'utf8', (err, data2) => {
      if (err) {
        console.error(`Error reading source file 2: ${err}`);
        return;
      }

      // Concatenate the contents of the two files
      const concatenatedContent = data1 + data2;

      // Write the concatenated content to the destination file
      fs.writeFile(destinationFile, concatenatedContent, 'utf8', (err) => {
        if (err) {
          console.error(`Error writing to destination file: ${err}`);
          return;
        }

        console.log('Files concatenated successfully!');
      });
    });
  });
;
