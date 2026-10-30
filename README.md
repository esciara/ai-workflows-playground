# ai-workflows-playground

Test bed for [esciara/ai-workflows](https://github.com/esciara/ai-workflows). Contains `minicart`, a tiny Python shopping-cart library (items, tax, coupons) with a pytest suite. Bugs are seeded here on purpose; seeded issues/PRs carry the `test-fixture` label.

## Develop

```sh
python3.12 -m venv .venv && . .venv/bin/activate
pip install -e '.[test]'
pytest
```
