# FacebookFilter
Simple app for filtering content from Facebook pages

# Core Use-Case

1. New user logs in via Facebook
2. User selects "Create New Filter"
3. User selects groups to filter from
4. User selects filter words - a filter word can be more than one word. e.g
   "Office Job"
5. User selects start date - only posts that were updated after this date will
   be shown
6. Filter is created
7. User looks over new posts and marks interesting/not and adds comments

# APIs

## Filter
Main API for configuring and changing filter parameters. This API is only
available for logged-in users. Each user can have a number of filters and the
filter id will be an ascending number for the user. So if a user has three
filters they are reachable in:
```
/api/filters/1
/api/filters/2
/api/filters/3
```

The available APIs and commands:

### /api/filters

* **GET** - Get list of available filters and their names
* **POST** - Create new filter. Returns the filter ID

## /api/filters/{id}

* **GET** - Get settings for the given filter id
* **PUT** - Update settings for the given filter

## /api/filters/{id}/new

* **GET** - New posts from the given filter. These posts were not marked by the
  user yet.

## /api/filters/{id}/kept

* **GET** - Posts marked for keeping

## /api/filters/{id}/thrown

* **GET** - Posts marked as uninteresting

# Database

The DB will hold the following main tables:

* User - A single user. Needed for Facebook connection. Will probably be the
  auth user models
* Filter - Filter settings for a specific user
* Posts - Contents of posts that were filtered. Each unique post will only have
  one row
* FilteredPost - Relation between a filter and a given post. Here each post will
  be marked as interesting/not and have the user's comments.

In more details it will be:

### FILTER

# Filter string

To create a complex filter for the post's contents we need a small and simple
query language. It will work something like this:

```
("city center" OR "nahlaot" OR "rehavia") AND NOT "sublet"
```

It will search in the posts' contents for the given words but filter out things
containing "sublet"
