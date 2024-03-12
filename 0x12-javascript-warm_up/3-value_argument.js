#!/usr/bin/node
onst arg = process.argv[2];

if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
