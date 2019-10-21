package com.bdp.mapreduce.duplicaterecord.mapper;

import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class DuplicateRecordMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
      private static final IntWritable recordValue = new IntWritable(1);
      
      @Override
      protected void map(LongWritable key, Text value,
                  Mapper<LongWritable, Text, Text, IntWritable>.Context context)
                  throws IOException, InterruptedException {
            if (key.get() == 0 && value.toString().contains("private_key")) {
                  return;
            } else 
                  context.write(value, recordValue);
      }
}

