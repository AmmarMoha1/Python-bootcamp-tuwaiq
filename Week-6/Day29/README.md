# Homework: URL Collision

### 1. What happens when I try to access a product with ID "create"?

If I visit:

`/products/create/`

Django will match the first URL pattern:

```python
path("products/create/", create_view)
```

So, it will call `create_view` instead of `details_view`.

This happens because Django checks the URL patterns from top to bottom and uses the first pattern that matches the URL.

---

### 2. How do I view product ID "create"?

With the current URL patterns, I cannot access a product with the ID `"create"` because `/products/create/` is already being used by `create_view`.

To solve this problem, I can change the create URL to something different, for example:

```python
path("products/new/", create_view)
path("products/<str:id>/", details_view)
```

Now:

`/products/new/` → `create_view`

`/products/create/` → `details_view` with `id = "create"`

So, I can access the product with ID `"create"` by visiting:

`/products/create/`

### Conclusion

Django checks URL patterns in order. Since `"create"` is a static URL and it comes before the dynamic `<str:id>` URL, Django matches it with `create_view`.

Changing `/products/create/` to `/products/new/` solves the URL collision and allows `"create"` to be used as a product ID.
