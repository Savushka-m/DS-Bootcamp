#!/bin/sh 
curl -s -k 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text=data+scientist' | jq > hh.json