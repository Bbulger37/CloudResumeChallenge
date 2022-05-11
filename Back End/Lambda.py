import boto3, json
client = boto3.resource('dynamodb')

    
def update_table(table, pk, sk):
    table = client.Table(table)
    response = table.update_item(
        Key = {pk: 1},
        UpdateExpression='ADD ' + sk + ' :incr',
        ExpressionAttributeValues={':incr': 1}
        )


    print(response)
    
def get_count(table, pk, sk):
    table = client.Table(table)
    response = table.get_item(
        Key = {pk: 1}
        )
    count = response['Item']   
    return(count)
    
def lambda_handler(event, context):
    update_table('Visits', 'VisitCount', 'vc')
    get_count('Visits', 'VisitCount', 'vc')
    
    return {
    'statusCode': 200,
    'headers': { "Access-Control-Allow-Origin": "*" },
    'body': get_count('Visits', 'VisitCount', 'vc')
    
    }