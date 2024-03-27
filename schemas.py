from marshmallow import Schema, fields




class GamesSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    description = fields.Str(dump_only=True)
    studio = fields.Str(dump_only=True)


class GenreSchema(Schema):
    id = fields.Str(dump_only=True)
    genre = fields.Str(dump_only=True)


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    first_name = fields.Str()
    last_name = fields.Str()


class GamesWithPostsSchemas(UserSchema):
    posts = fields.List(fields.Nested(GamesSchema), dump_only=True)

class GenreWithPostsSchemas(GenreSchema):
    posts = fields.List(fields.Nested(GenreSchema), dump_only=True)

class UserWithPostsSchemas(UserSchema):
    posts = fields.List(fields.Nested(UserSchema), dump_only=True)