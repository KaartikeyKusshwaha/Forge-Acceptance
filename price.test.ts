import {test} from 'node:test';
import assert from 'node:assert/strict';
import {computePrice} from './price.ts';
test('default discount', () => assert.equal(computePrice(50),45));
test('explicit discount', () => assert.equal(computePrice(100,20),80));
