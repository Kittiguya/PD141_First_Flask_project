from marshmallow import Schema, fields




class GamesSchemas(Schema):
    name = fields.Str(dump_only=True)
    description = fields.Str(dump_only=True)
    studio = fields.Str(dump_only=True)


class GenreSchemas(Schema):
    genre = fields.Str(dump_only=True)


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    first_name = fields.Str()
    last_name = fields.Str()


class GamesWithPostsSchemas(GamesSchemas):
    posts = fields.List(fields.Nested(GamesSchemas), dump_only=True)

class GenreWithPostsSchemas(GenreSchemas):
    posts = fields.List(fields.Nested(GenreSchemas), dump_only=True)

class UserWithPostsSchemas(UserSchema):
    posts = fields.List(fields.Nested(UserSchema), dump_only=True)