package mysqlJavaES;

// import org.elasticsearch.action.bulk.BulkRequestBuilder;
// import org.elasticsearch.action.bulk.BulkResponse;
// import org.elasticsearch.action.index.IndexRequestBuilder;
// import org.elasticsearch.action.search.SearchResponse;
// import org.elasticsearch.client.Client;
// import org.elasticsearch.common.xcontent.XContentBuilder;
// import org.elasticsearch.index.query.QueryBuilders;
// import org.elasticsearch.search.SearchHit;
// import storm.trident.state.State;
//
// import static org.elasticsearch.common.xcontent.XContentFactory.jsonBuilder;

import org.elasticsearch.action.bulk.BackoffPolicy;
import org.elasticsearch.action.bulk.BulkProcessor;
import org.elasticsearch.common.unit.ByteSizeUnit;
import org.elasticsearch.common.unit.ByteSizeValue;
import org.elasticsearch.common.unit.TimeValue;
import java.io.IOException;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class JavaES {

  public static void main(String args[]){
    List<Long> ids = new ArrayList();
    for(int i=11;i<30;i++){
      ids.add(i);
    }
    List<String> names = new ArrayList();
    for(int i=11;i<30;i++){
      names.add("shashank" + i);
    }
    ElasticSearchJavaBulk elasticSearchJavaBulk = new ElasticSearchJavaBulk();
    elasticSearchJavaBulk.bulkIndex(ids, names);
  }

  public void bulkIndex(List<Long> tweetIds, List<String> tweets) {
  //       BulkRequestBuilder requestBuilder = client.prepareBulk();
  //       for(int i = 0; i < tweetIds.size(); i++) {
  //           XContentBuilder builder;
  //           try {
  //               builder = jsonBuilder()
  //                       .startObject()
  //                       .field("text", tweets.get(i))
  //                       .field("id", tweetIds.get(i))
  //                       .endObject();
  //           } catch (IOException e) {
  //               continue;
  //           }
  //           IndexRequestBuilder request = client.prepareIndex("hackaton", "tweets")
  //                   .setIndex("hackaton")
  //                   .setType("tweets")
  //                   .setSource(builder);
  //           requestBuilder.add(request);
  //       }
  //       BulkResponse bulkResponse = requestBuilder.execute().actionGet();
  //       int items = bulkResponse.getItems().length;
  //       System.err.print("indexed [" + items + "] items, with failures? [" + bulkResponse.hasFailures()  + "]");

  BulkProcessor bulkProcessor = BulkProcessor.builder(
          client,
          new BulkProcessor.Listener() {
              @Override
              public void beforeBulk(long executionId,
                                     BulkRequest request) {
                                     logger.info("Going to execute new bulk composed of {} actions", request.numberOfActions());
                                   }

              @Override
              public void afterBulk(long executionId,
                                    BulkRequest request,
                                    BulkResponse response) {
                                      logger.info("Executed bulk composed of {} actions", request.numberOfActions());
                                  }

              @Override
              public void afterBulk(long executionId,
                                    BulkRequest request,
                                    Throwable failure) {
                                    logger.warn("Error executing bulk", failure);
                                  }
          })
          .setBulkSize(new ByteSizeValue(1, ByteSizeUnit.GB))
          .setFlushInterval(TimeValue.timeValueSeconds(5))
          .setBulkActions(10000)
          .setConcurrentRequests(1)
          .setBackoffPolicy(
              BackoffPolicy.exponentialBackoff(TimeValue.timeValueMillis(100), 3))
          .build();

          bulkProcessor.add()
    }
}
