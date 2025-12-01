# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
-----------------------------------------------------------------------
Step-by-step when server_name = 'server2'

Call get_server_status('server2').

In the function: server_config.get(server_name, {}) → this is server_config.get('server2', {}).

Since 'server2' exists as a key in server_config, .get(...) returns its associated inner dictionary:
{'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'}.

On that inner dictionary, the code does .get('status', 'Server not found'). That’s the same as inner_dict.get('status', ...).

The 'status' key exists inside that inner dict, so .get(...) returns "inactive".

The function returns "inactive".

So status = "inactive".

Finally, print(f"{server_name} status: {status}") prints:

server2 status: inactive


So the numerical / concrete result is "inactive" for that call with 'server2'.

If you try with a non-existent key, e.g. 'server4', then:

server_config.get('server4', {}) returns {} (the default).

On that {}, .get('status', 'Server not found') returns the default "Server not found".

So you’d get "Server not found" safely, without a KeyError.

Using .get(..., {}) is a good pattern to safely attempt nested-dictionary lookups. 
Justin Okumu
+1
