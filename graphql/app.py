from flask import Flask, request, jsonify
from ariadne import QueryType, gql, load_schema_from_path, make_executable_schema, graphql_sync
from ariadne.asgi import GraphQL
from ariadne.constants import PLAYGROUND_HTML

from resolvers import hello, bye

query = QueryType()

type_defs = load_schema_from_path('schema.graphql')

query.set_field('hello', hello)
query.set_field('bye', bye) 

schema = make_executable_schema(type_defs, query)

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()
    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)