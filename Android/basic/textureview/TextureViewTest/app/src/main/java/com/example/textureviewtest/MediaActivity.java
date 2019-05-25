package com.example.textureviewtest;

import android.graphics.SurfaceTexture;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Environment;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Surface;
import android.view.SurfaceHolder;
import android.view.TextureView;
import android.view.View;
import android.widget.Toast;

import java.io.File;
import java.io.IOException;

public class MediaActivity extends AppCompatActivity implements TextureView.SurfaceTextureListener, MediaPlayer.OnPreparedListener{
    private String videoPath = Environment.getExternalStorageDirectory().getPath() + "/101.mp4";
    private TextureView textureView;
    private MediaPlayer mediaPlayer;

    private SurfaceTexture mTexture;
    private SurfaceHolder holder;
    private Surface surface;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_media);

        textureView = findViewById(R.id.textureView);
        //注册一个SurfaceTexture，用于监听SurfaceTexure
        textureView.setSurfaceTextureListener(this);

        File file = new File(this.videoPath);
        if (! file.exists()) {
            Toast.makeText(this, "MediaActivity", Toast.LENGTH_LONG).show();
            Log.d("MediaActivity", this.videoPath + " not exists");
        } else {
            Toast.makeText(this, "MediaActivity", Toast.LENGTH_LONG).show();
            Log.d("MediaActivity", this.videoPath + " exists");
        }
    }

    /**
     * 播放视频的入口，当SurfaceTexure可得到时被调用
     */
    private void playVideo() {
        if (mediaPlayer == null) {
            mTexture = textureView.getSurfaceTexture();
            surface = new Surface(mTexture);
            initMediaPlayer();
        }
    }

    private void initMediaPlayer() {
        this.mediaPlayer = new MediaPlayer();
        try {
            mediaPlayer.setDataSource(videoPath);
            mediaPlayer.setSurface(surface);
            mediaPlayer.prepareAsync();
            mediaPlayer.setOnPreparedListener(this);
            mediaPlayer.setLooping(true);
        } catch (IllegalArgumentException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        } catch (SecurityException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        } catch (IllegalStateException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        } catch (IOException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }
    }

    @Override
    public void onPrepared(MediaPlayer mp) {
        try {
            if (mp != null) {
                mp.start(); //视频开始播放
            }
        } catch (IllegalStateException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (textureView.isAvailable()) {
            playVideo();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (mTexture != null) {
            mTexture.release();  //停止视频的绘制线程
        }
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer =null;
        }
    }

    @Override
    public void onSurfaceTextureAvailable(SurfaceTexture surface, int width, int height) {
        playVideo();
    }

    @Override
    public void onSurfaceTextureSizeChanged(SurfaceTexture surface, int width, int height) {

    }

    @Override
    public boolean onSurfaceTextureDestroyed(SurfaceTexture surface) {
        return false;
    }

    @Override
    public void onSurfaceTextureUpdated(SurfaceTexture surface) {

    }
}
