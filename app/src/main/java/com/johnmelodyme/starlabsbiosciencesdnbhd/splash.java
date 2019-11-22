package com.johnmelodyme.starlabsbiosciencesdnbhd;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

public class splash extends AppCompatActivity {

    int timing;

    {
        timing = 0;
    }

    Handler hand;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        hand = new Handler();
        hand.postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent toMain;
                toMain = new Intent(splash.this, MainActivity.class);
                startActivity(toMain);
                finish();
            }
        }, 2000);
    }
}
