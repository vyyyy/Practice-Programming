package com.example.android.howtojavascript;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.Collections;
import java.util.List;

/**
 * Created by vypatz on 17/11/2015.
 */
public class RecyclerAdapter extends RecyclerView.Adapter<RecyclerAdapter.ViewHolder> {
    List<Information> mDataset = Collections.emptyList();

    // public static final String EXTRA_TEXT = "some text";


    // Provide a reference to the views for each data item
    // Complex data items may need more than one view per item, and
    // you provide access to all the views for a data item in a view holder
    public static class ViewHolder extends RecyclerView.ViewHolder {
        // each data item is just a string in this case
        public TextView mTextView;
        public ViewHolder(View v) {
            super(v);
            mTextView = (TextView) v.findViewById(R.id.list_item);
        }
    }

    // Provide a suitable constructor (depends on the kind of dataset)
    public RecyclerAdapter(List<Information> myDataset) {
        mDataset = myDataset;
    }

    // Create new views (invoked by the layout manager)
    @Override
    public RecyclerAdapter.ViewHolder onCreateViewHolder(ViewGroup parent,
                                                         int viewType) {
        // create a new view
        View v = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.fragment_part_three, parent, false);
        ViewHolder vh = new ViewHolder(v);
        return vh;
    }

    // Replace the contents of a view (invoked by the layout manager)
    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        // - get element from your dataset at this position
        // - replace the contents of the view with that element
        Information current = mDataset.get(position);
        holder.mTextView.setText(current.info);

        /*vh.mTextView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Context context = view.getContext();
                TextView clickedTextView = (TextView) view.findViewById(R.id.textview);
                String text = clickedTextView.getText().toString();

                if (text == mDataset[0]) {
                    text += "\nnumbers code";
                } else if (text == myArray[1]) {
                    text += "\nstrings code";
                } else if (text == myArray[2]) {
                    text += "\nbooleans code";
                } else if (text == myArray[3]) {
                    text += "\narrays code";
                } else if (text == myArray[4]) {
                    text += "\nobjects code";
                } else if (text == myArray[5]) {
                    text += "\nvariables code";
                } else if (text == myArray[6]) {
                    text += "\nfunctions";
                } else if (text == myArray[7]) {
                    text += "\nmethods";
                } else if (text == myArray[8]) {
                    text += "\nif-condition";
                } else if (text == myArray[9]) {
                    text += "\nfor loop";
                } else if (text == myArray[10]) {
                    text += "\nfor-in loop";
                } else if (text == myArray[11]) {
                    text += "\nwhile loop";
                } else if (text == myArray[12]) {
                    text += "\ndo/while loop";
                } else if (text == myArray[13]) {
                    text += "\nthis";
                } else if (text == myArray[14]) {
                    text += "\ncustom constructors";
                } else {
                    text += "\nbuilt-in methods";
                }

                Intent intent = new Intent(context, DetailActivity.class);
                intent.putExtra(EXTRA_TEXT, text);
                context.startActivity(intent);

            }
        });*/

    }

    // Return the size of your dataset (invoked by the layout manager)

    @Override
    public int getItemCount() {
        return 3;
    }
}
