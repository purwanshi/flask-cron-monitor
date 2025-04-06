#!/bin/bash
echo"(date)-compute triggered" >>  /home/princess/cronlog.txt
curl -s http://127.0.0.1/compute > //dev/null
