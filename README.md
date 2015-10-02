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
available for logged-in users. Each user can have a number of filters and will
only be able to view and edit the ones he created.

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
  auth user model
* FacebookPage - Name and ID of a facebook page, group or person we can
  subscribe to
* Filter - Filter settings for a specific user
* FilterFacebookPage - Connection between a filter and the pages it's following
* Post - Contents of posts that were filtered. Each unique post will only have
  one row
* FilteredPost - Relation between a filter and a given post. Here, each post
  will be marked as interesting/not and have the user's comments.

## Column Details

### FACEBOOK_PAGE

| Name | Type | Description            |
|:-----|:-----|:-----------------------|
| ID   | Str  | Facebook object id     |
| Name | Str  | Page/Group/User's name |

### FILTER

| Name      | Type | Description              |
|:----------|:-----|:-------------------------|
| ID        | Int  | Filter id                |
| User      | FK   | Relation to user         |
| FilterStr | Str  | The search string to use |

### FILTER_FACEBOOK_PAGE

| Name     | Type | Description |
|:---------|:-----|:------------|
| FilterID | Int  | Filter id   |
| PageID   | Str  | Page id     |

### POST

| Name         | Type | Description                                      |
|:-------------|:-----|:-------------------------------------------------|
| ID           | Str  | Facebook's post ID. Usually {group_id}_{post_id} |
| Message      | Str  | The post's text                                  |
| User         | Str  | Posting user name                                |
| Created Time | Time | When was the post created                        |
| Updated Time | Time | When was the post last updated                   |
| PageID       | Str  | Page this post came from                         |

### FILTERED_POST

| Name        | Type | Description                            |
|:------------|:-----|:---------------------------------------|
| FilterID    | FK   | Relation to filter                     |
| PostID      | FK   | Relation to post                       |
| Found Time  | Time | When has the filter found this post    |
| Interesting | Bool | Is this post interesting (can be null) |
| Comment     | Str  | User comment for this post             |


# Filter string

We should be able to have complex filtering like:

*Find all posts that contain the words "Apartment" and "Roof" except if the word
"Sublet" exists*

This could be created using a small query language or a JSON format. But at
first we'll only support searching for multiple strings with **OR** between
them. This will be created using a simple JSON array object:

```json
["city center", "uptown", "downtown"]
```

Which will translate to: *Find all posts that contain "city center" or "uptown"
or "downtown"*
