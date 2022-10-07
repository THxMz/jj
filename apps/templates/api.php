
require __DIR__ . '/vendor/autoload.php';

use FacebookAds\Object\AdAccount;
use FacebookAds\Object\Campaign;
use FacebookAds\Api;
use FacebookAds\Logger\CurlLogger;

$access_token = '<ACCESS_TOKEN>';
$app_secret = '<APP_SECRET>';
$app_id = '<APP_ID>';
$id = '<AD_ACCOUNT_ID>';

$api = Api::init($app_id, $app_secret, $access_token);
$api->setLogger(new CurlLogger());

$fields = array(
);
$params = array(
  'name' => 'My campaign',
  'objective' => 'LINK_CLICKS',
  'status' => 'PAUSED',
  'special_ad_categories' => array(),
);
echo json_encode((new AdAccount($id))->createCampaign(
  $fields,
  $params
)->exportAllData(), JSON_PRETTY_PRINT);

